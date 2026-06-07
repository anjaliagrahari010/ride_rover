from django.contrib import admin
from .models import LoginUser, Provider, Vehicle, BookVehicle, Inquiry, Booking

admin.site.register(LoginUser)
admin.site.register(Provider)
admin.site.register(Vehicle)
admin.site.register(BookVehicle)
admin.site.register(Inquiry)

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('booking_id', 'booking_type', 'pickup_date', 'dropoff_date', 'total_amount', 'created_at')
    search_fields = ('booking_id', 'booking_type')
    list_filter = ('booking_type',)