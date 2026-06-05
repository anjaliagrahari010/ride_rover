from django.urls import path
from .import views
from user.models import *

urlpatterns=[
   path('clientapp/',views.clientdash,name="clientdash"),
    path('clientapp/booking_history/', views.booking_history, name='booking_history'),
    path('clientapp/booking/cancel/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
]