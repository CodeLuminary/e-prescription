from django.shortcuts import render
from .addPatientForm import AddPatientForm
from .models import Patient, Prescription, PrescriptionItem
from pharmacist.models import Drug
from datetime import datetime

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .prescriptionSerializer import PrescriptionSerializers, PrescriptionItemSerializers

def getAllData():
    drugs = Drug.objects.all()
    patient = Patient.objects.all()
    return {
        "drugs": drugs,
        "patients": patient
    }

# Create your views here.
def index(request):
    return render(request, 'doctor/index.html', {"data": getAllData()})

def addpatient(request):
    form = AddPatientForm(request.POST)

    if(form.is_valid()):
        try:
            full_name = form.cleaned_data['full_name']
            email = form.cleaned_data['email']
            phone_no = form.cleaned_data['phone_no']
            age = form.cleaned_data['age']
            patient_id = form.cleaned_data['patient_id']
            gender = form.cleaned_data['gender']

            newPatient = Patient(full_name = full_name,
                                 email = email,number=phone_no,
                                 age = age,
                                 patient_no = patient_id,
                                 gender = gender)
            newPatient.save()
            print(newPatient)
            #print(newPatient.id)

            return render(request, "doctor/index.html", {
                "status": True,
                "message": "Patient added successfully",
                "data": getAllData()
            })

        except:
            #print('not working')
            return render(request, "doctor/index.html", {
                "status": False,
                "message": "Action failed. Patient could not be added",
                "data": getAllData()
            })
    
    else: 
        #print('horible')
        return render(request, "doctor/index.html",{"data": getAllData()})

@api_view(['POST'])
def prescribeDrug(request):
    try:
        now = datetime.now()
        presId = str(int(now.timestamp()))
        patient = Patient.objects.get(id=int(request.data['patient_id']))
        prescribe = Prescription(
            purpose = request.data['purpose'],
            patient = patient,
            date_time = datetime.now(),
            prescription_id = presId,
            prescribe_by_id = 1
        )
        prescribe.save()
        for d in request.data['drugs']:
            drug = Drug.objects.get(id=int(d['id']))
            pDrug = PrescriptionItem(
                prescription = prescribe,
                drug_id = drug,
                no_of_unit = d['unit']    
            )
            pDrug.save()
        print('succeed')
        return Response({"message":"Prescription made successfully", "data": presId})
    except:       
        return Response({"message":"Action failed"})
    