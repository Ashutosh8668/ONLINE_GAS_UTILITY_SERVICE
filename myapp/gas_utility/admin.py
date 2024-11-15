from django.contrib import admin
from .models import ServiceRequest

@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('type', 'status', 'created_at', 'resolved_at')
    list_filter = ('status',)
    search_fields = ('type', 'details')
    date_hierarchy = 'created_at'