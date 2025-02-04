from django.contrib import admin
from .models import ContactMessage

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')  # Add created_at field here

admin.site.register(ContactMessage, ContactMessageAdmin)
