from django.contrib import admin
from user.models import Registration
from user.models import *

class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'name', 'booking_type', 'pickup_date', 'dropoff_date', 'total_amount')
