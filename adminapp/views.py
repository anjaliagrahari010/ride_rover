from django.shortcuts import render,redirect,get_object_or_404
import datetime
from user.models import *
from .forms import *
from django.http import JsonResponse
from datetime import datetime

def index(request):
    if 'username' in request.session:
        total_users = User.objects.count()
        total_vehicles = Vehicle.objects.count()
        total_bookings = Booking.objects.count()
        total_inquiries = Inquiry.objects.count()

    context = {
        'total_users': total_users,
        'total_vehicles': total_vehicles,
        'total_bookings': total_bookings,
        'total_inquiries': total_inquiries,
    }

    return render(request, 'adminhome.html', context)
    
    

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
           
            customer = Registration(
                fullname=form.cleaned_data['fullname'],
                email=form.cleaned_data['emailid'],
                mob_number=form.cleaned_data['mob_number'],
                licensenumber=form.cleaned_data['licensenumber'],
                licensepic=form.cleaned_data['licensepic'],
                userpic=form.cleaned_data['userpic'],
                signpic=form.cleaned_data['signpic']
            )
            customer.save()
            return redirect('success')  
    else:
        form = RegistrationForm()

    return render(request, 'registration.html', {'form': form})

def custmng(request):
    users = Registration.objects.all()  
    context = {
        'users': users,
    }
    return render(request, 'custmng.html', {'users': users})

def logout(request):
    
    return redirect('ride')

def delcust(request,id):
    try:
        if request.session['username']!=None:
            Registration.objects.get(id=id).delete()
            return redirect('adminapp:custmng')
    except:
        return redirect('ride')

def provider(request):
    try:
        if request.session['username']!=None:
            p=Provider.objects.all()
            if request.method=="POST":
                name=request.POST['name']
                email=request.POST['email']
                phone=request.POST['phone']
                address=request.POST['address']
                vehicle_name=request.POST['vehicle_name']
                vehicle_number=request.POST['vehicle_number']
                year=request.POST['year']
                date_joined=request.POST['date_joined']
                is_active=request.POST['is_active']
                provider_img=request.POST['provider_image']
                vehicle_img=request.POST['vehicle_image']
                p=Provider(name=name,email=email,phone=phone, address=address, vehicle_name=vehicle_name,vehicle_number=vehicle_number,year=year, date_joined = date_joined,is_active = is_active, provider_img = provider_img, vehicle_img=vehicle_img )
                p.save()
                return redirect('adminapp:provider')
            return render(request,'provider.html',locals())
    except:
            return(redirect('ride'))
        
def delprovider(request,id):
     try:
          if request.session['username']!=None:
               Provider.objects.get(id=id).delete()
               return redirect('adminapp:provider')
     except:
          return redirect('ride')
     
def inquiry_admin_view(request):
    inquiries = Inquiry.objects.all().order_by('-submitted_at')  
    return render(request, 'admin_inquiries.html', {'inquiries': inquiries})

def vehicle(request):
    vehicle = Vehicle.objects.all()
    return render(request, 'vehicle.html', {'vehicle':vehicle} )

def delvehicle(request,id):
     try:
          if request.session['username']!=None:
               Vehicle.objects.get(id=id).delete()
               return redirect('adminapp:Vehicle')
     except:
          return redirect('ride')

def booking_details(request):
    bookings = Booking.objects.all() 
    return render(request, "bookings_details.html", {"bookings": bookings})

