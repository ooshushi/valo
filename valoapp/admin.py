from django.contrib import admin
from valoapp.models import Agent, Map, Weapon, Player, MatchResult

# admin.site.register(Agent)
# Register your models here.

@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'created_at', 'updated_at',)
    search_fields = ('name',)
    
@admin.register(Map)
class MapAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at',)
    search_fields = ('name',)

@admin.register(Weapon)
class WeaponAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'created_at', 'updated_at',)
    search_fields = ('name',)

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('username', 'team', 'created_at', 'updated_at',)
    search_fields = ('name',)

@admin.register(MatchResult)
class MatchResultAdmin(admin.ModelAdmin):
    list_display = ('map_played', 'winner', 'loser', 'match_date', 'created_at', 'updated_at',)
    search_fields = ('name',)
