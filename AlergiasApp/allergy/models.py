from django.db import models



class Allergy(models.Model):
    nameAllergy = models.CharField(max_length=200)


class  Patient(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateTimeField('date of birth')
    sex = models.CharField(max_length=1)
    address = models.CharField(max_length=200)
    allergy =  models.ForeignKey(Allergy, on_delete=models.CASCADE)