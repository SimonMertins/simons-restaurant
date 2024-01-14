from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Table, Booking
from datetime import datetime, timedelta
from django.contrib.auth import login
from .forms import SignUpForm, UserProfileForm


def view_home(request):
    # Implement logic for the home view
    return render(request, 'restaurant_booking/home.html')


# Placeholder context,
context = {}


def view_available_time_slots(request):
    # Implement logic to fetch and display available time slots
    # For demonstration purposes, let's assume tables are available from 6 PM to 10 PM in 1-hour slots
    start_time = datetime.strptime('18:00', '%H:%M').time()
    end_time = datetime.strptime('22:00', '%H:%M').time()
    time_slots = [start_time + timedelta(hours=i)
                  for i in range((end_time.hour - start_time.hour))]

    # Fetch available tables (assuming tables are available for the entire duration)
    available_tables = Table.objects.filter(is_available=True)

    context = {
        'time_slots': time_slots,
        'available_tables': available_tables,
    }
    return render(request, 'restaurant_booking/available_time_slots.html', context)


def make_reservation(request):
    # Implement logic to handle reservation submissions
    if request.method == 'POST':
        # Get form data from the request
        selected_time = request.POST.get('selected_time')
        selected_table_id = request.POST.get('selected_table')

        # Convert selected_time to a datetime object for the Booking model
        reservation_datetime = datetime.combine(
            datetime.today(), datetime.strptime(selected_time, '%H:%M').time())

        # Check if the selected table is available at the chosen time
        selected_table = Table.objects.get(pk=selected_table_id)
        if selected_table.is_available:
            # Create a reservation
            reservation = Booking.objects.create(
                user=request.user,  # Assuming the user is authenticated
                table=selected_table,
                date=reservation_datetime.date(),
                time=reservation_datetime.time(),
                guests=1  # Placeholder value, replace with the actual number of guests
            )

            # Update table availability
            selected_table.is_available = False
            selected_table.save()

            # Redirect to a success page or display a success message
            return HttpResponse("Reservation successful!")

    # If not a POST request or if the reservation fails, redirect to the available time slots page
    return redirect('available_time_slots')


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
