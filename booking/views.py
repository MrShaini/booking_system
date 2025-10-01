from django.shortcuts import render, redirect
from .models import House, Booking
from auth_system.models import CustomUser
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    houses = House.objects.all()
    return render(request, "index.html/", context={"houses": houses})

@login_required
def house_detail(request, pk):
    house = House.objects.get(id=pk)
    return render(request, "house_detail.html", context={"house": house})

@login_required
def booking_house(request, pk):
    if request.method == "GET":
        house = House.objects.get(id=pk)
        context = {
            "house": house,
        }
        return render(request, "booking_house.html", context=context)
    else:

        arrival_date = request.POST.get("arrival_date")
        departure_date = request.POST.get("departure_date")
        comment = request.POST.get("comment")
        house = House.objects.get(id=pk)

        
        Booking.objects.create(
            client=request.user,
            house=house,
            arrival_date=arrival_date,
            departure_date=departure_date,
            comment=comment,
        )
        return redirect("index")
    
@login_required
def all_bookings_by_user(request):
    bookings = Booking.objects.filter(client=request.user)
    return render(request, "bookings", context={"bookings":
    bookings})