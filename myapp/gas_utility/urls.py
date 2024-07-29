from django.urls import path
from gas_utility import views

urlpatterns = [
    path('submit/', views.submit_request, name='submit_request'),
    path('', views.track_request, name='track_request'),
    path('manage/', views.manage_requests, name='manage_requests'),
    path('resolve/<int:request_id>/', views.resolve_request, name='resolve_request'),
]