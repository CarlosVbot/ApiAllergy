from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview , name="api-overview"),
    path('allergy-list/<str:pk>', views.taskDetailsAllergy , name="allergy-task-list"),
    path('allergy-create/', views.taskCreateAllergy, name="allergy-task-create"),
    path('allergy-update/<str:pk>/', views.taskUpdateAllergy, name="allergy-task-update"),
    path('allergy-delete/<str:pk>/', views.taskDeleteAllergy, name="allergy-task-delete"),

    path('patient-list/<str:pk>', views.taskDetailsPatient , name="patient-task-list"),
    path('patient-create/', views.taskCreatePatient, name="patient-task-create"),
    path('patient-update/<str:pk>/', views.taskUpdatePatient, name="patient-task-update"),
    path('patient-delete/<str:pk>/', views.taskDeletePatient, name="patient-task-delete")
]