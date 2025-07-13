# Pseudo-code: Budget Management System (Django + Celery)

## Objective

To design a backend system for an Ad Agency that manages brand ad campaigns by tracking spend, enforcing budget limits, enabling/disabling campaigns based on rules, and resetting spend periodically.

---

## Data Models (High-Level)

### Brand

* **name**: Name of the brand
* **daily\_budget**: Maximum allowed spend per day
* **monthly\_budget**: Maximum allowed spend per month
* **is\_active**: Determines if the brand is currently active

### Campaign

* **brand**: Foreign key linking to Brand
* **name**: Campaign title
* **is\_active**: Indicates if the campaign is live
* **total\_daily\_spend**: Running total of today’s spend
* **total\_monthly\_spend**: Running total of current month's spend
* **allowed\_start\_hour**: Hour of day campaign is allowed to start (0-23)
* **allowed\_end\_hour**: Hour of day campaign must end (0-23)

### Spend

* **campaign**: Foreign key linking to Campaign
* **date**: Date of spend
* **amount**: Amount spent on the campaign

---

## Core Logic (High-Level)

### 1. Spend Tracking

* On each spend event:

  * Record a new `Spend` with campaign, date, and amount.
  * Increment `total_daily_spend` and `total_monthly_spend` on the campaign.

### 2. Budget Enforcement

* In a periodic Celery task:

  * Loop through all `Campaign` instances that are `is_active=True`.
  * Pause the campaign if:

    * `total_daily_spend` ≥ `brand.daily_budget`
    * OR `total_monthly_spend` ≥ `brand.monthly_budget`

### 3. Dayparting Enforcement

* During periodic Celery task:

  * For each active campaign:

    * Check if `current_hour` falls between `allowed_start_hour` and `allowed_end_hour`.
    * If not, pause the campaign.

### 4. Daily & Monthly Budget Resets

* A Celery task that runs at midnight:

  * Resets `total_daily_spend` of all campaigns.
  * If it's the first day of the month:

    * Reset `total_monthly_spend`.
  * Reactivate campaigns where:

    * spend is within allowed budget.
    * and current time is within dayparting.

### 5. Dashboard View

* Render list of brands and campaigns.
* Include real-time spend data for the current day.
* Display budget status and flags.

### 6. Health Check View

* Simple endpoint that returns a "System is healthy" message for uptime checks.

---

## Periodic Celery Tasks

### check\_and\_pause\_campaigns

* Runs every few minutes.
* Pauses campaigns that:

  * Exceed brand budget
  * Fall outside allowed time window

### reset\_daily\_monthly\_spend (To be implemented)

* Runs at midnight daily.
* Resets daily and monthly spend counters.
* Reactivates eligible campaigns.

---

## Assumptions & Simplifications

* External process is responsible for logging spend events.
* Campaigns are paused by setting `is_active=False`.
* Campaigns are resumed only if all conditions are re-satisfied.
* All time-related logic assumes the same timezone (UTC).

---

## Optional Enhancements

* Add timezone awareness per brand/campaign
* Integrate alert system for budget breaches
* Add admin dashboard filters for spend insights
* Add audit log to record pause/resume events
