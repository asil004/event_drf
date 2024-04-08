from django.contrib import admin

from event.models import Item, Event, EventDetail, UserEvent, EventImage

admin.site.register(Item)

admin.site.register(EventDetail)
admin.site.register(UserEvent)


class EventsImgAdmin(admin.TabularInline):
    model = EventImage


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    inlines = [EventsImgAdmin]
