from django.db import models

from account.models import Users
from pharmacist.models import Drug

# Create your models here.
class Patient(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    number = models.TextField()
    age = models.IntegerField()
    gender = models.TextField(max_length=10)
    patient_no = models.TextField()

class Prescription(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    prescription_id = models.TextField()
    date_time = models.DateTimeField()
    prescribe_by = models.ForeignKey(Users, on_delete=models.CASCADE)
    purpose = models.TextField(default='')

class PrescriptionItem(models.Model):
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE)
    drug_id = models.ForeignKey(Drug, on_delete=models.CASCADE)
    no_of_unit = models.IntegerField()

class PrescriptionService(models.Model):
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE)
    date_served = models.DateTimeField()
    served_by = models.ForeignKey(Users, on_delete=models.DO_NOTHING)
