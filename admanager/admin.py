from django.contrib import admin
from .models import Brand, Campaign, Spend

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'daily_budget', 'monthly_budget', 'is_active')

@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'brand', 'is_active', 'total_daily_spend', 'total_monthly_spend',
        'allowed_start_hour', 'allowed_end_hour'
    )
    list_filter = ('is_active', 'brand')

@admin.register(Spend)
class SpendAdmin(admin.ModelAdmin):
    list_display = ('campaign', 'date', 'amount')
    list_filter = ('campaign', 'date')
