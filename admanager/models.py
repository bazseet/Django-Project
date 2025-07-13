from django.db import models
from django.utils import timezone
from typing import Optional

class Brand(models.Model):
    """A brand with a daily and monthly ad budget."""
    name: str = models.CharField(max_length=255)
    daily_budget: float = models.FloatField()
    monthly_budget: float = models.FloatField()
    is_active: bool = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name

class Campaign(models.Model):
    """An advertising campaign linked to a brand."""
    brand: Brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='campaigns')
    name: str = models.CharField(max_length=255)
    is_active: bool = models.BooleanField(default=True)
    total_daily_spend: float = models.FloatField(default=0.0)
    total_monthly_spend: float = models.FloatField(default=0.0)
    allowed_start_hour: int = models.IntegerField(default=0)   # e.g., 9 for 9AM
    allowed_end_hour: int = models.IntegerField(default=23)    # e.g., 17 for 5PM

    def __str__(self) -> str:
        return self.name

    def is_within_dayparting(self, dt: Optional[timezone.datetime] = None) -> bool:
        """
        Check if the campaign is within its scheduled hours (dayparting).
        """
        now = dt or timezone.now()
        current_hour = now.hour
        return self.allowed_start_hour <= current_hour < self.allowed_end_hour

class Spend(models.Model):
    """A spend record for a campaign on a specific date."""
    campaign: Campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name='spends')
    date: timezone.datetime = models.DateField()
    amount: float = models.FloatField(default=0.0)

    def __str__(self) -> str:
        return f"{self.campaign.name} - {self.date}: ${self.amount}"
