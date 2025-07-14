# Budget Management System

A Django + Celery-based system to manage advertising campaign budgets for brands.  
It tracks ad spend, enforces daily/monthly budgets, applies dayparting rules, and resets budgets automatically.

---

## 🚀 Features

- ✅ Track daily and monthly ad spend per campaign.
- ✅ Automatically pause campaigns exceeding their budget.
- ✅ Enforce dayparting schedules (hour-based activation).
- ✅ Reset budgets daily and monthly.
- ✅ Admin interface for managing brands, campaigns, and spends.
- ✅ Dashboard and health check views.
- ✅ Static typing with `mypy` support.

---

## 🧠 Project Objective

This project was built as a **coding challenge** to:

> Implement a backend system using Django and Celery that:
> - Tracks daily/monthly ad spend.
> - Pauses/activates campaigns based on budget limits and time windows.
> - Performs resets and reactivations periodically using Celery.
> - Maintains static typing and clarity throughout.

---

## 🗃️ Data Models

### Brand
- `name`: str  
- `daily_budget`: float  
- `monthly_budget`: float  
- `is_active`: bool  

### Campaign
- `brand`: FK to Brand  
- `name`: str  
- `is_active`: bool  
- `total_daily_spend`: float  
- `total_monthly_spend`: float  
- `allowed_start_hour`: int  
- `allowed_end_hour`: int  

### Spend
- `campaign`: FK to Campaign  
- `date`: date  
- `amount`: float  

---

## 🛠️ Setup Instructions

### 1. Clone and install dependencies

```bash
git clone https://github.com/bazseet/budget-management-system.git
cd "Django Project directory"
python -m venv venv
venv\Scripts\activate  # On Windows
pip install -r requirements.txt



**## Run Migrations**

python manage.py makemigrations
python manage.py migrate


### Create Superuser
python manage.py createsuperuser


## Run the Server
python manage.py runserver


## Run Celery Worker to ensure redis is running
celery -A django_celery_budget worker -l info

## Run Celery Beat to run periodic tasks
celery -A django_celery_budget beat -l info




 System Workflow
check_and_pause_campaigns: Periodic Celery task.

Pauses campaigns exceeding budgets or outside allowed hours.

reset_daily_monthly_spend (to be added):

Resets daily/monthly spend.

Reactivates eligible campaigns.

Views:

/ = Dashboard

/health/ = Health check page

 Type Checking
This project includes static type hints and can be checked using mypy:


mypy .
Zero type errors expected. See mypy.ini for config.

 Related Files
pseudocode.md: High-level system design.

mypy.ini: Static typing configuration.



📝 Assumptions
Campaigns are logged and updated externally.

Timezone is UTC by default.

Budgets are inclusive of the threshold.

🛠️ Tech Stack
Django 5.2.4

Celery

Redis

SQLite (default, can swap with PostgreSQL)

Python 3.10+

 Author
Abdul Imran Ajikanle



