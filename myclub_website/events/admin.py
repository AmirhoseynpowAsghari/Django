from django.contrib import admin
from .models import Event
from .models import Venue
from .models import MyClubUser





admin.site.register(MyClubUser)


@admin.register(Venue)

class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'zip_code', 'phone', 'web', 'email_address')
    ordering = ('name',)
    search_fields = ('name', 'address')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fields = (('name', 'venue'), 'event_date', 'description', 'manager')
    list_display = ('name', 'venue', 'event_date', 'description', 'manager')
    list_filter = ('event_date', 'venue')
    ordering = ('-event_date',)