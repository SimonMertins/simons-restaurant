"""
URL configuration for simons_restaurant project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from restaurant_booking import views as restaurant_views
from restaurant_booking.views import get_available_time_slots


urlpatterns = [
    path('', restaurant_views.view_home, name='home'), 
    path('available-time-slots/', restaurant_views.view_available_time_slots, name='available_time_slots'),
    path('make-reservation/', restaurant_views.make_reservation, name='make_reservation'),
    path('manage-bookings/', restaurant_views.manage_bookings, name='manage_bookings'),
    path('reservations/', restaurant_views.view_reservations, name='view_reservations'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('get_available_time_slots/', get_available_time_slots, name='get_available_time_slots'),
    path('menu/', restaurant_views.view_menu, name='menu'),
    path('contact/', restaurant_views.contact, name='contact'),



]
