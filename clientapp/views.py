from django.shortcuts import render,redirect, get_object_or_404, reverse
import datetime
from django.contrib.auth.decorators import login_required
from user.models import*
# from django.views.decorators.cache import cache_control
# from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
def clientdash(request):
    return render(request,'clienthome.html')

@login_required
def booking_history(request):
    
    bookings = Booking.objects.filter(user=request.user).order_by('-pickup_date')

     

    return render(request, 'booking_history.html', {'bookings':bookings})


def cancel_booking(request, booking_id):
    
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)

    if request.method == 'POST':
        booking.status = 'Cancelled'
        booking.save()
        return redirect('clientapp:client_dashboard')

    return render(request, 'cancel_booking.html', {'booking': booking})