from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    path('packages/', views.packages, name='packages'),
    path('destination/', views.destination, name='destination'),
    path('gallery/', views.gallery, name='gallery'),
    path('booking/', views.booking, name='booking'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    path('delete-booking/<int:id>/', views.delete_booking, name='delete_booking'),
    path('update-booking-status/<int:id>/', views.update_booking_status, name='update_booking_status'),

]