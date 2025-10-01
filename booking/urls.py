from django.urls import path
from .views import index, house_detail, booking_house, all_bookings_by_user

urlpatterns = [
    path("index/", index, name="index"),
    path("", index, name="index"),
    path("houses/<int:pk>/", house_detail, name="house-detail"),
    path("houses/<int:pk>/booking/", booking_house, name="booking-house"),
    path("bookings/", all_bookings_by_user, name="bookings"),
]