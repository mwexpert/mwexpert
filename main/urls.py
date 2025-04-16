from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    # Serve index.html as the landing page at the root URL
    path('', views.index, name='index'),  # Root URL that shows the landing page

    # Other pages
    path('home/', views.home, name='home'),  # Optional: If you still want a separate /home page
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('industries/', views.industries, name='industries'),
    path('why-us/', views.why_us, name='why_us'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('careers/', views.careers, name='careers'),
    path('insights/', views.insights, name='insights'),
    path('contact/', views.contact, name='contact'),
    path('pricing/', views.pricing, name='pricing'),
    path('faqs/', views.faqs, name='faqs'),

    # Admin page
    path('admin/', admin.site.urls),
]
