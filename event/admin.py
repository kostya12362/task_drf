from django.contrib import admin

# Register your models here.

from event.models import EventType, Event


@admin.register(EventType)
class EventTypeAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('user', 'event_type', 'info', 'timestamp', 'created_at')
    list_filter = ('event_type', 'timestamp')