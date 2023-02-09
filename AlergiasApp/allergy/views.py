from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import  AllergySerializer , PatientSerializer
from .models import Allergy, Patient
import json

@api_view(['GET'])
def apiOverview(request):
    tasks = Patient.objects.all().order_by('-id')
    serializer = PatientSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def taskDetailsAllergy(request,pk):
    tasks = Allergy.objects.get(id=pk)
    serializer = AllergySerializer(tasks,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def taskCreateAllergy(request):
	serializer = AllergySerializer(data = request.body)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)
    
@api_view(['PUT'])
def taskUpdateAllergy(request, pk):
	task = Allergy.objects.get(id=pk)
	serializer = AllergySerializer(instance=task, data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

@api_view(['DELETE'])
def taskDeleteAllergy(request, pk):
	task = Allergy.objects.get(id=pk)
	task.delete()
	return Response('Allergy succsesfully delete!')


@api_view(['GET'])
def taskDetailsPatient(request,pk):
    tasks = Patient.objects.get(id=pk)
    serializer = PatientSerializer(tasks,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def taskCreatePatient(request):
	serializer = PatientSerializer(data = request.body)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)
    
@api_view(['PUT'])
def taskUpdatePatient(request, pk):
	task = Patient.objects.get(id=pk)
	serializer = PatientSerializer(instance=task, data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

@api_view(['DELETE'])
def taskDeletePatient(request, pk):
	task = Patient.objects.get(id=pk)
	task.delete()
	return Response('Patient succsesfully delete!')