from django.utils.decorators import method_decorator
from django.http import HttpResponse 
from .models import Allergy, Patient
from django.views import View
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

class AllergyView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self,request ,*args , **kwargs):
        return super().dispatch(request,*args,**kwargs)
    
    def get(self,request,id=0):
        if request.body:
            jd = json.loads(request.body)
        else:
            jd = {}

        if 'type' in jd:
            if jd['type'] == 'patient':
                if id>0:
                    patients = list(Patient.objects.filter(id=id).values())
                    if len(patients) < 1:
                        datos = {'messasge': 'No results'}
                    else:
                        datos = {'messasge': 'success',  'patients':patients}
                    return JsonResponse(datos)
                else:
                    patients = list(Patient.objects.values())
                    if len(patients) < 1:
                        datos = {'messasge': 'No results'}
                    else:
                        datos = {'messasge': 'success','patients':patients}                  
                    return JsonResponse(datos)
            elif jd['type'] == "allergy":
                if id>0:
                    Allergys = list(Allergy.objects.filter(id=id).values())
                    if len(Allergys) < 1:
                        datos = {'messasge': 'No results'}
                    else:
                        datos = {'messasge': 'success',  'Allergy':Allergys}
                    return JsonResponse(datos)
                else:
                    Allergys = list(Allergy.objects.values())
                    if len(Allergys) < 1:
                        datos = {'messasge': 'No results'}
                    else:
                        datos = {'messasge': 'success',  'Allergy':Allergys}
                    return JsonResponse(datos)
        else:            
            patients = list(Patient.objects.values())
            allergys = list(Allergy.objects.values())
            if len(patients) > 0:
                datos = {'messasge': 'success', 'patients':patients, 'allergys':allergys}
            else:
                datos = {'messasge': 'patients not founds'}
            return JsonResponse(datos)
            
       
            

    def post(self,request):
        jd = json.loads(request.body)
        if 'type' in jd:
            if jd['type']=='patient':
                Patient.objects.create(name = jd['name'], date= jd['date'],sex= jd['sex'], address = jd['address'],allergy_id=jd['allergy'])
                return JsonResponse ({'messasge': 'Patient create'})
            elif jd['type']=='allergy':
                Allergy.objects.create(nameAllergy = jd['name'])
                return JsonResponse ({'messasge': 'Allergy create'})
            else:    
                return JsonResponse ({'messasge': 'type no found ...'})
        else:
            return JsonResponse({'messasge': 'body not has type ...'})

    def put(self,request,id=0):
        if request.body:
            jd = json.loads(request.body)
        else:
            return JsonResponse({'messasge': 'not has body ...'})
        if 'type' in jd:
            if jd['type'] == 'patient':
                patients = list(Patient.objects.filter(id=id).values())
                print(patients)
                if len(patients) < 1:
                    datos = {'messasge': 'No results'}
                else:
                    patient =  Patient.objects.get(id=id)  
                    patient.name = jd['name']  
                    patient.date = jd['date'] 
                    patient.sex = jd['sex'] 
                    patient.address = jd['address'] 
                    patient.allergy_id = jd['allergy'] 
                    patient.save()
                    datos = {'messasge': 'edit complete1'}
                return JsonResponse(datos)
            elif jd['type'] == "allergy":
                Allergys = list(Allergy.objects.filter(id=id).values())
                if len(Allergys) < 1:
                        datos = {'messasge': 'No results'}
                        return JsonResponse(datos)
                else:
                        Allergys =  Allergy.objects.get(id=id)  
                        Allergys.nameAllergy = jd['name']  
                        Allergys.save()
                        datos = {'messasge': 'edit complete'}
                return JsonResponse(datos)
            else:
                return JsonResponse({'messasge': 'body not has type ...'})

        else:
            return JsonResponse({'messasge': 'body not has type ...'})
    
    def delete(self,request,id=0):
        if request.body:
            jd = json.loads(request.body)
        else:
            jd = {}

        if 'type' in jd:
            if jd['type'] == 'patient':
                if id>0:
                    patients = list(Patient.objects.filter(id=id).values())
                    if len(patients) > 0:
                        Patient.objects.filter(id=id).delete()
                        datos = {'messasge': 'complete'}
                        return JsonResponse(datos)
                else:                  
                    datos = {'messasge': 'bad id'}                  
                    return JsonResponse(datos)
            elif jd['type'] == "allergy":
                if id>0:
                    Allergys = list(Allergy.objects.filter(id=id).values())
                    if len(Allergys) > 0:
                        Allergy.objects.filter(id=id).delete()
                        datos = {'messasge': 'complete'}
                    else:
                        datos = {'messasge': 'bad id'}
                    return JsonResponse(datos)
                else:
                    datos = {'messasge': 'bad id'}
                    return JsonResponse(datos)