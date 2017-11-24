from django.contrib import admin

from core.models import Kind, Team, Tournament


@admin.register(Kind)
class KindAdmin(admin.ModelAdmin):
    pass


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    pass


@admin.register(Tournament)
class TournamentAdmin(admin.ModelAdmin):
    filter_horizontal = ("teams", )
