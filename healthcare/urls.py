from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import *

urlpatterns = [
    path('auth/register/', RegisterView.as_view()),
    path('auth/login/', TokenObtainPairView.as_view()),

    path('patients/', PatientListCreateView.as_view()),
    path('patients/<int:pk>/', PatientRetrieveUpdateDestroyView.as_view()),

    path('doctors/', DoctorListCreateView.as_view()),
    path('doctors/<int:pk>/', DoctorRetrieveUpdateDestroyView.as_view()),

    path('mappings/', MappingListCreateView.as_view()),
    path('mappings/<int:patient_id>/', MappingByPatientView.as_view()),
    path('mappings/delete/<int:pk>/', MappingDeleteView.as_view()),

    path('auth/refresh/', TokenRefreshView.as_view()),
]
