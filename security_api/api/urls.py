from django.urls import path
from .views import GoogleScanView

urlpatterns = [
    path('scan/google/', GoogleScanView.as_view(), name='google_scan'),
]