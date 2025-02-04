from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=255)  # User's Name
    email = models.EmailField()  # User's Email
    message = models.TextField()  # Message Content
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically stores timestamp

    def __str__(self):
        return f"Message from {self.name} ({self.email}) at {self.created_at}"
