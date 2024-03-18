from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Table, Booking, MenuItem
from datetime import datetime, timedelta
from django.contrib.auth import login
from .forms import ReservationForm
from django.template.context_processors import csrf
from .models import Reservation



def view_home(request):
    # Implement logic for the home view
    return render(request, 'restaurant_booking/home.html')

def view_available_time_slots(request):
    # Implement logic to fetch and display available time slots
    start_time = datetime.strptime('12:00', '%H:%M').time()
    end_time = datetime.strptime('20:00', '%H:%M').time()
    time_slots = [start_time + timedelta(hours=i) for i in range((end_time.hour - start_time.hour))]

    # Fetch available tables (assuming tables are available for the entire duration)
    available_tables = Table.objects.filter(is_available=True)

    context = {
        'time_slots': time_slots,
        'available_tables': available_tables,
    }
    return render(request, 'restaurant_booking/available_time_slots.html', context)

def make_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)

            # Convert selected time to a datetime object for the Booking model
            reservation_datetime = datetime.combine(
                reservation.date, reservation.time
            )

            # Check if the selected table is available at the chosen time
            selected_table = Table.objects.get(pk=reservation.table.id)
            if selected_table.is_available:
                # Save the reservation
                reservation.save()

                # Update table availability
                selected_table.is_available = False
                selected_table.save()

                # Return a JSON response indicating success
                return JsonResponse({'status': 'success', 'message': 'Reservation successful!'})
            else:
                # Table is not available, include a message in the context
                return JsonResponse({'status': 'error', 'message': 'Selected table is not available at the chosen time.'})
        else:
            # Form is not valid, include it in the context to display errors
            form_errors = form.errors.as_data()
            return JsonResponse({'status': 'error', 'message': 'Invalid form submission.', 'errors': form_errors})

    # If not a POST request, redirect to the available time slots page
    csrf_token = csrf(request)['csrf_token']
    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})


def view_reservations(request):
    return render(request, 'restaurant_booking/reservations.html')

def manage_bookings(request):
    user_bookings = Booking.objects.filter(user=request.user)

    context = {
        'user_bookings': user_bookings,
    }
    return render(request, 'restaurant_booking/manage_bookings.html', context)

def get_available_time_slots(request):
    selected_date = request.GET.get('date')
    available_time_slots = ['12:00 PM', '1:00 PM', '6:00 PM', '7:00 PM']

    return JsonResponse(available_time_slots, safe=False)

def view_menu(request):

    MenuItem.objects.all().delete()

    MenuItem.objects.create(name='Margherita Pizza', price=12.99)
    MenuItem.objects.create(name='Chicken Alfredo Pasta', price=15.99)
    MenuItem.objects.create(name='Grilled Salmon', price=18.99)
    MenuItem.objects.create(name='Caesar Salad', price=8.99)
    MenuItem.objects.create(name='Chocolate Brownie Sundae', price=7.99)

    MenuItem.objects.create(name='Soda', price=2.99)
    MenuItem.objects.create(name='Iced Tea', price=1.99)
    MenuItem.objects.create(name='Mango Smoothie', price=4.99)
    MenuItem.objects.create(name='Espresso', price=3.49)

    menu_items = MenuItem.objects.all()
    return render(request, 'restaurant_booking/menu.html', {'menu_items': menu_items})

def contact(request):
    return render(request, 'restaurant_booking/contact.html')