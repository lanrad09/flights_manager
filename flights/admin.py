from django.contrib import admin
from .models import Flight, Airport, Passenger
# Register your models here.
#to customize the admin interface (read Django documentation), create a class for the settings
class FlightAdmin(admin.ModelAdmin):
    #Define what field to have access to in the list_display
    list_display = ("id", "origin", "destination", "duration")

class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal = ("flights",)

admin.site.register(Airport)
admin.site.register(Flight, FlightAdmin) #register the flight and ask it to use the FlightAdmin setting
admin.site.register(Passenger, PassengerAdmin)