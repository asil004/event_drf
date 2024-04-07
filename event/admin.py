from django.contrib import admin

from event.models import Item, Event, EventDetail, UserEvent

admin.site.register(Item)

admin.site.register(EventDetail)
admin.site.register(UserEvent)


class ItemsAdmin(admin.TabularInline):
    model = Item


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    inlines = [ItemsAdmin]
