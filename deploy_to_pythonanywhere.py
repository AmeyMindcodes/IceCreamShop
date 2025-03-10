#!/usr/bin/env python
"""
Helper script for deploying to PythonAnywhere
This script will:
1. Collect static files
2. Apply migrations
3. Create a superuser if needed
"""

import os
import sys
import django
from django.core.management import call_command

def main():
    print("Setting up Django environment...")
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'IceCreamShop.settings')
    django.setup()
    
    print("\n1. Collecting static files...")
    call_command('collectstatic', '--noinput')
    
    print("\n2. Applying migrations...")
    call_command('migrate', '--noinput')
    
    # Check if we need to create a superuser
    from django.contrib.auth import get_user_model
    User = get_user_model()
    
    if not User.objects.filter(is_superuser=True).exists():
        print("\n3. Creating a superuser...")
        username = input("Enter username (default: admin): ") or "admin"
        email = input("Enter email: ")
        
        from django.contrib.auth.management.commands.createsuperuser import Command as CreateSuperUserCommand
        from django.core.management.base import CommandError
        
        try:
            password = input("Enter password: ")
            confirm_password = input("Confirm password: ")
            
            if password != confirm_password:
                print("Passwords don't match!")
                return
            
            user = User.objects.create_superuser(username=username, email=email, password=password)
            print(f"Superuser '{username}' created successfully!")
        except Exception as e:
            print(f"Error creating superuser: {e}")
    else:
        print("\n3. Superuser already exists, skipping creation.")
    
    print("\nDeployment setup complete! Your site should be ready to go.")
    print("Don't forget to reload your web app in the PythonAnywhere dashboard.")

if __name__ == "__main__":
    main() 