from django.shortcuts import render, redirect
from .models import ContactMessage
from .models import ContactMessage, Booking
from django.db.models import Count
from django.shortcuts import render, redirect, get_object_or_404


def index(request):
    return render(request, 'server/home.html')

def about(request):
    return render(request, 'server/about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        return render(request, 'server/contact.html', {
            'success': 'Your message has been sent successfully!'
        })

    return render(request, 'server/contact.html')

def services(request):
    return render(request, 'server/services.html')

def packages(request):
    return render(request, 'server/packages.html')

def destination(request):
    return render(request, 'server/destination.html')

def gallery(request):
    return render(request, 'server/gallery.html')
def booking(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        package = request.POST.get('package')
        travel_date = request.POST.get('travel_date')
        persons = request.POST.get('persons')

        Booking.objects.create(
            name=name,
            email=email,
            phone=phone,
            package=package,
            travel_date=travel_date,
            persons=persons
        )

        return render(request, 'server/booking.html', {
            'success': 'Your booking has been submitted successfully!'
        })

    return render(request, 'server/booking.html')

def my_bookings(request):
    all_bookings = Booking.objects.all().order_by('-id')

    total_bookings = all_bookings.count()
    total_travellers = sum(b.persons for b in all_bookings)

    package_report = all_bookings.values('package').annotate(
        total=Count('id')
    ).order_by('-total')

    search = request.GET.get('search', '')
    selected_package = request.GET.get('package', '')

    bookings = all_bookings

    if search:
        bookings = bookings.filter(name__icontains=search)

    if selected_package:
        bookings = bookings.filter(package=selected_package)

    packages = all_bookings.values_list(
        'package', flat=True
    ).distinct()

    return render(request, 'server/my_bookings.html', {
        'bookings': bookings,
        'total_bookings': total_bookings,
        'total_travellers': total_travellers,
        'package_report': package_report,
        'packages': packages,
        'search': search,
        'selected_package': selected_package
    })

def delete_booking(request, id):
    booking = get_object_or_404(Booking, id=id)

    if request.method == 'POST':
        booking.delete()
        return redirect('my_bookings')

    return redirect('my_bookings')

def update_booking_status(request, id):
    if request.method == 'POST':
        booking = get_object_or_404(Booking, id=id)
        new_status = request.POST.get('status')

        if new_status in ['Pending', 'Confirmed', 'Cancelled']:
            booking.status = new_status
            booking.save()

    return redirect('my_bookings')