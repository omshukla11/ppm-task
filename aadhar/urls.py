from django.urls import path
from .views import *

urlpatterns = [
    path('activity/<str:act>/',AadharFilterAPI.as_view(), name='Aadhar Active & Inactive List'),
    path('',AadharAPI.as_view(), name='Aadhar Details'),
    path('address/',AddressAPI.as_view(), name='All Address'),
    path('address/<int:pk>/', AddressDetailAPI.as_view(), name='Address Update & Delete'),
    path('qualification/',QualificationAPI.as_view(), name='Aadhar Details'),
    path('qualification/<int:pk>/',QualificationDetailAPI.as_view(),name='All Qualification'),
    path('bank/',BankAPI.as_view(), name='Aadhar Details'),
    path('bank/<int:pk>/',BankDetailAPI.as_view(),name='Qaulification Details'),
    path('perdet/',PerDetAPI.as_view(), name='Aadhar Details'),
    path('perdet/<int:pk>/',PerDetAPIRUD.as_view(),name='Qaulification Details'),
    path('allinfo/<str:adh>/',AllInfoAPI.as_view(),name="All info API")
]
