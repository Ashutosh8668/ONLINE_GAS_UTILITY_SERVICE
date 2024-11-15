from django.db import models

class ServiceRequest(models.Model):
    STATUS_CHOICES = (
        ('pending', 'pending'),
        ('In_progress', 'In_progress'),
        ('completed', 'completed'),
    )
    type = models.CharField(max_length=100)
    details = models.TextField()
    attachment = models.FileField(upload_to="attachments/")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(null=True, blank=True)
    
class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    account_number = models.CharField(max_length=20)
