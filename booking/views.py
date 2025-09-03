from django.shortcuts import render
from .models import House

def index(request):
    houses = House.objects.all()
    return render(request, "index.html/", context={"houses": houses})

def house_detail(request, pk):
    house = House.objects.get(id=pk)
    return render(request, "house_detail.html", context={"house": house})