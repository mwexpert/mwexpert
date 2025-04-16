from django.shortcuts import render

# Landing page view (index.html)
def index(request):
    return render(request, 'main/index.html')  # Render the landing page (index.html)

# About page view
def home(request):
    return render(request, 'main/home.html')  # Render the landing page
def about(request):
    return render(request, 'main/about.html')

# Services page view
def services(request):
    return render(request, 'main/services.html')

# Industries page view
def industries(request):
    return render(request, 'main/industries.html')

# Why Us page view
def why_us(request):
    return render(request, 'main/why_us.html')

# Testimonials page view
def testimonials(request):
    return render(request, 'main/testimonials.html')

# Careers page view
def careers(request):
    return render(request, 'main/careers.html')

# Insights page view
def insights(request):
    return render(request, 'main/insights.html')

# Contact page view
def contact(request):
    return render(request, 'main/contact.html')

# Pricing page view
def pricing(request):
    return render(request, 'main/pricing.html')

# FAQs page view
def faqs(request):
    return render(request, 'main/faqs.html')
