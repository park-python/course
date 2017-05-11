from django.contrib import admin

from core.models import Country, Auto, Label, Dealer#, Sale


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    pass


@admin.register(Auto)
class AutoAdmin(admin.ModelAdmin):
    pass


@admin.register(Dealer)
class DealerAdmin(admin.ModelAdmin):
    pass


@admin.register(Label)
class LabelAdmin(admin.ModelAdmin):
    pass


# @admin.register(Sale)
# class SaleAdmin(admin.ModelAdmin):
#     pass
