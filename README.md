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
