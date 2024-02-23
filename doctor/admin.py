from django.contrib import admin

# Register your models here.
from .models import Patient, Prescription, PrescriptionItem, PrescriptionService

admin.site.register(Patient)
admin.site.register(Prescription)
admin.site.register(PrescriptionItem)
admin.site.register(PrescriptionService)