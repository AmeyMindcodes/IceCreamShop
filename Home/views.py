from django.shortcuts import render, redirect
from django.contrib import messages
from .models import IceCreamFlavor, Order, Gallery

# Home Page
def home(request):
    # Get featured flavors for the homepage
    featured_flavors = IceCreamFlavor.objects.filter(featured=True)[:3]
    
    context = {
        'featured_flavors': featured_flavors,
        'page_title': 'Home'
    }
    return render(request, 'index.html', context)

# About Page
def about(request):
    context = {
        'page_title': 'About Us'
    }
    return render(request, 'about.html', context)

# Services Page
def services(request):
    context = {
        'page_title': 'Our Services'
    }
    return render(request, 'services.html', context)

# Contact Page
def contact(request):
    if request.method == "POST":
        # Process the contact form
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # Create a new contact message
        from .models import ContactMessage
        ContactMessage.objects.create(
            name=name,
            email=email,
            message=message
        )
        
        messages.success(request, "Your message has been sent! We'll get back to you soon.")
        return redirect('contact')
    
    context = {
        'page_title': 'Contact Us'
    }
    return render(request, 'contact.html', context)

# Gallery Page
def gallery(request):
    # Get all gallery images
    gallery_images = Gallery.objects.all()
    
    context = {
        'gallery_images': gallery_images,
        'page_title': 'Gallery'
    }
    return render(request, 'gallery.html', context)

# Menu Page (Combined with Flavors)
def menu(request):
    # Get all flavors categorized
    regular_flavors = IceCreamFlavor.objects.filter(category='regular')
    premium_flavors = IceCreamFlavor.objects.filter(category='premium')
    seasonal_flavors = IceCreamFlavor.objects.filter(category='seasonal')
    
    context = {
        'regular_flavors': regular_flavors,
        'premium_flavors': premium_flavors,
        'seasonal_flavors': seasonal_flavors,
        'page_title': 'Our Menu'
    }
    return render(request, 'flavors.html', context)

# Visit Page (Replaces Order Page)
def visit(request):
    context = {
        'page_title': 'Visit Our Store'
    }
    return render(request, 'visit.html', context)
