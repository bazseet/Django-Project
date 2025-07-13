from celery import shared_task
from django.utils import timezone
from .models import Campaign

@shared_task
def check_and_pause_campaigns() -> None:
    now = timezone.now()
    for campaign in Campaign.objects.filter(is_active=True):
        if (
            campaign.total_daily_spend >= campaign.brand.daily_budget
            or campaign.total_monthly_spend >= campaign.brand.monthly_budget
            or not campaign.is_within_dayparting(now)
        ):
            campaign.is_active = False
            campaign.save()
