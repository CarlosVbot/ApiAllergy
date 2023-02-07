from django.urls import path
from .views import AllergyView

urlpatterns = [
    path('lista/', AllergyView.as_view(), name='allergy_list'),
    path('lista/<int:id>', AllergyView.as_view(), name='allergy_process')
]