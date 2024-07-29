from django.shortcuts import render, redirect, get_object_or_404
from .models import ServiceRequest
from django.utils import timezone


def submit_request(request):
    if request.method == 'POST':
        type = request.POST.get('type')
        details = request.POST.get('details')
        attachment = request.FILES.get('attachment')
        ServiceRequest.objects.create(type=type, details=details, attachment=attachment)
        return redirect('track_request')

    return render(request, 'submit_request.html')

def track_request(request):
    service_requests = ServiceRequest.objects.all()
    return render(request, 'track_request.html', {'service_requests': service_requests})

def manage_requests(request):

    pending_requests = ServiceRequest.objects.exclude(status='Completed')
    completed_requests = ServiceRequest.objects.filter(status='Completed')
    
    context = {
        'pending_requests': pending_requests,
        'completed_requests': completed_requests
    }
    return render(request, 'manage_requests.html', context)

def resolve_request(request, request_id):
    service_request = get_object_or_404(ServiceRequest, pk=request_id)

    if request.method == 'POST':
        service_request.status = 'Completed'
        service_request.resolved_at = timezone.now()
        service_request.save()
        return redirect('manage_requests')

    return render(request, 'resolve_request.html', {'service_request': service_request})