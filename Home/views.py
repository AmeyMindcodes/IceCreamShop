from django.shortcuts import render, HttpResponse, redirect
from .models import ContactMessage  # Import the ContactMessage model
from django.contrib import messages

# Home Page
def index(request):
    context = {
        'variable1': 'Hello World',
        'variable2': 'Welcome to Django'
    }
    return render(request, 'index.html', context)

# About Page
def about(request):
    return render(request, 'about.html')

# Services Page
def services(request):  
    return render(request, 'services.html')

# Contact Page
def contact(request):
    return render(request, 'contact.html')

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
