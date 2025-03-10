from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=255)  # User's Name
    email = models.EmailField()  # User's Email
    message = models.TextField()  # Message Content
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically stores timestamp

    def __str__(self):
        return f"Message from {self.name} ({self.email}) at {self.created_at}"

class IceCreamFlavor(models.Model):
    CATEGORY_CHOICES = [
        ('regular', 'Regular'),
        ('premium', 'Premium'),
        ('seasonal', 'Seasonal'),
    ]
    
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='flavors/', null=True, blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='regular')
    available = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    
    customer_name = models.CharField(max_length=255)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=20)
    flavor = models.ForeignKey(IceCreamFlavor, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    delivery_address = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    order_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Order #{self.id} - {self.customer_name} - {self.status}"
    
    @property
    def total_price(self):
        return self.flavor.price * self.quantity

class Gallery(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='gallery/')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Galleries"
