from django.contrib import admin
from .models import ContactMessage, IceCreamFlavor, Order, Gallery

# Register the ContactMessage model
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email', 'message')
    list_filter = ('created_at',)
    readonly_fields = ('created_at',)

# Register the IceCreamFlavor model
@admin.register(IceCreamFlavor)
class IceCreamFlavorAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'available', 'featured')
    list_filter = ('category', 'available', 'featured')
    search_fields = ('name', 'description')
    list_editable = ('available', 'featured', 'price')

# Register the Order model
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_name', 'flavor', 'quantity', 'status', 'order_date')
    list_filter = ('status', 'order_date')
    search_fields = ('customer_name', 'customer_email', 'customer_phone')
    list_editable = ('status',)

# Register the Gallery model
@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'description')
    list_filter = ('created_at',)
    readonly_fields = ('created_at',)
