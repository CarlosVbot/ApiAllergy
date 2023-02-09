from django.test import TestCase
from django.urls import reverse, resolve
from django.test import SimpleTestCase
from allergy.views import apiOverview
from rest_framework.test import APITestCase
from rest_framework import status
from allergy.models import Allergy, Patient

class AllergyAPITest(APITestCase):

    def test_taskCreateAllergy(self):
        data = {"nameAllergy":"prueba test"}
        response = self.client.post("/allergy/allergy-create/",data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_taskDetailsAllergy(self):
        Allergy.objects.create(nameAllergy = 'test')
        response = self.client.get(reverse("allergy-task-list",kwargs = {"pk":1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
     
    def test_apiOverview(self):
        response = self.client.get("/allergy/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_taskUpdateAllergy(self):
        Allergy.objects.create(nameAllergy = 'test')
        data = {"nameAllergy":"prueba test 2"}
        response = self.client.put(reverse("allergy-task-update",kwargs = {"pk":1}),data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_taskDeleteAllergy(self):
        Allergy.objects.create(nameAllergy = 'test')
        response = self.client.delete(reverse("allergy-task-delete",kwargs = {"pk":1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_taskCreatePatient(self):
        Allergy.objects.create(nameAllergy = 'test')
        data = {"type":"patient","name":"pablo","date":"2019-04-01T21:49:56Z","sex":"M","address":"test","allergy":1}
        response = self.client.post("/allergy/patient-create/",data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_taskDetailsPatient(self):
        Allergy.objects.create(nameAllergy = 'test')
        Patient.objects.create( name = 'tito' ,date = "2019-04-01T21:49:56Z",sex="M",address='asas',allergy_id=1 )
        response = self.client.get(reverse("patient-task-list",kwargs = {"pk":1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_taskUpdatePatient(self):
        Allergy.objects.create(nameAllergy = 'test')
        Patient.objects.create( name = 'tito' ,date = "2019-04-01T21:49:56Z",sex="M",address='asas',allergy_id=1 )
        response = self.client.put(reverse("patient-task-update",kwargs = {"pk":1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
     
    def test_taskDeletePatient(self):
        Allergy.objects.create(nameAllergy = 'test')
        Patient.objects.create( name = 'tito' ,date = "2019-04-01T21:49:56Z",sex="M",address='asas',allergy_id=1 )
        response = self.client.delete(reverse("patient-task-delete",kwargs = {"pk":1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
