from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Table, Booking
from datetime import datetime, timedelta
from django.contrib.auth import login
from .forms import SignUpForm, UserProfileForm, ReservationForm
from django.template.context_processors import csrf
from django.http import JsonResponse
from .models import Reservation 

def view_home(request):
    # Implement logic for the home view
    return render(request, 'restaurant_booking/home.html')

def view_available_time_slots(request):
    # Implement logic to fetch and display available time slots
    # For demonstration purposes, let's assume tables are available from 6 PM to 10 PM in 1-hour slots
    start_time = datetime.strptime('18:00', '%H:%M').time()
    end_time = datetime.strptime('22:00', '%H:%M').time()
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

            # Additional processing if needed
            reservation.user = request.user  # Assuming the user is authenticated

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

                print("Reservation successful!")

                # Redirect to a success page or display a success message
                return render(request, 'restaurant_booking/reservations.html', {'reservation_success': 'Reservation successful!', 'form': ReservationForm()})
            else:
                # Table is not available, include a message in the context
                return render(request, 'restaurant_booking/reservations.html', {'reservation_error': 'Selected table is not available at the chosen time.', 'form': form})
        else:
            # Form is not valid, include it in the context to display errors
            return render(request, 'restaurant_booking/reservations.html', {'form': form, 'reservation_error': 'Invalid form submission. Please check the form and try again.'})

    # If not a POST request, redirect to the available time slots page
    csrf_token = csrf(request)['csrf_token']
    return render(request, 'restaurant_booking/reservations.html', {'csrf_token': csrf_token, 'form': ReservationForm()})

def view_reservations(request):
    return render(request, 'restaurant_booking/reservations.html')

def manage_bookings(request):
    # Implement logic to display and manage bookings
    # For demonstration purposes, let's fetch all bookings for the logged-in user
    # Assuming the user is authenticated
    user_bookings = Booking.objects.filter(user=request.user)

    context = {
        'user_bookings': user_bookings,
    }
    return render(request, 'restaurant_booking/manage_bookings.html', context)

# for user registration form
def register(request):
    if request.method == 'POST':
        user_form = SignUpForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            login(request, user)  # Log in the user after registration
            # Redirect to the home page after successful registration
            return redirect('home')
    else:
        user_form = SignUpForm()
        profile_form = UserProfileForm()

    return render(request, 'registration/register.html', {'user_form': user_form, 'profile_form': profile_form})

def get_available_time_slots(request):
    selected_date = request.GET.get('date')
    available_time_slots = ['12:00 PM', '1:00 PM', '6:00 PM', '7:00 PM']

    return JsonResponse(available_time_slots, safe=False)

