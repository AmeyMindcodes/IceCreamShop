from django.shortcuts import render, HttpResponse, redirect
from .models import ContactMessage, IceCreamFlavor, Order  # Import the models
from django.contrib import messages

# Home Page
def index(request):
    # Get featured flavors for the homepage
    featured_flavors = IceCreamFlavor.objects.filter(featured=True)[:3]
    
    context = {
        'featured_flavors': featured_flavors,
        'page_title': 'Welcome to Ice Cream Wonderland'
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
    context = {
        'page_title': 'Contact Us'
    }
    return render(request, 'contact.html', context)

# Handle Contact Form Submission
def send_message(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Save the message to the database
        ContactMessage.objects.create(name=name, email=email, message=message)
        messages.success(request, "Your message has been sent!")

        # Redirect back to the contact page with a success message
        return redirect('/contact')

    return HttpResponse("Invalid Request", status=400)

# Menu Page
def menu(request):
    # Get all flavors for the menu page
    all_flavors = IceCreamFlavor.objects.all()
    
    context = {
        'flavors': all_flavors,
        'page_title': 'Our Menu'
    }
    return render(request, 'menu.html', context)

# Gallery Page
def gallery(request):
    context = {
        'page_title': 'Our Gallery'
    }
    return render(request, 'gallery.html', context)

# Flavors Page
def flavors(request):
    # Get all flavors categorized
    regular_flavors = IceCreamFlavor.objects.filter(category='regular')
    premium_flavors = IceCreamFlavor.objects.filter(category='premium')
    seasonal_flavors = IceCreamFlavor.objects.filter(category='seasonal')
    
    context = {
        'regular_flavors': regular_flavors,
        'premium_flavors': premium_flavors,
        'seasonal_flavors': seasonal_flavors,
        'page_title': 'Our Flavors'
    }
    return render(request, 'flavors.html', context)

# Order Page
def order(request):
    # Get all available flavors for ordering
    available_flavors = IceCreamFlavor.objects.filter(available=True)
    
    if request.method == "POST":
        # Process the order form
        customer_name = request.POST.get('customer_name')
        customer_email = request.POST.get('customer_email')
        customer_phone = request.POST.get('customer_phone')
        flavor_id = request.POST.get('flavor')
        quantity = request.POST.get('quantity')
        delivery_address = request.POST.get('delivery_address')
        
        # Create a new order
        flavor = IceCreamFlavor.objects.get(id=flavor_id)
        Order.objects.create(
            customer_name=customer_name,
            customer_email=customer_email,
            customer_phone=customer_phone,
            flavor=flavor,
            quantity=quantity,
            delivery_address=delivery_address
        )
        
        messages.success(request, "Your order has been placed successfully!")
        return redirect('/')
    
    context = {
        'flavors': available_flavors,
        'page_title': 'Order Now'
    }
    return render(request, 'order.html', context)
