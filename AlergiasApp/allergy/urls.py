from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview , name="api-overview"),
    path('allergy-list/<str:pk>', views.taskDetailsAllergy , name="task-list"),
    path('allergy-create/', views.taskCreateAllergy, name="task-create"),
    path('allergy-update/<str:pk>/', views.taskUpdateAllergy, name="task-update"),
    path('allergy-delete/<str:pk>/', views.taskDeleteAllergy, name="task-delete"),

    path('patient-list/<str:pk>', views.taskDetailsPatient , name="task-list"),
    path('patient-create/', views.taskCreatePatient, name="task-create"),
    path('patient-update/<str:pk>/', views.taskUpdatePatient, name="task-update"),
    path('patient-delete/<str:pk>/', views.taskDeletePatient, name="task-delete")
]