from django.shortcuts import render
from .addPatientForm import AddPatientForm
from .models import Patient
from pharmacist.models import Drug

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
    