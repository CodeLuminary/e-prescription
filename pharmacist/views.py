from django.shortcuts import render
from .addDrugForm import AddDrugForm
from .models import Drug
from rest_framework.response import Response
from rest_framework.decorators import api_view
from doctor.models import Prescription, PrescriptionItem
from doctor.prescriptionSerializer import PrescriptionSerializers, PrescriptionItemSerializers, PrescriptionResultSerializer, PrescriptionItemResultSerializer

def getDrugs():
    return Drug.objects.all()

# Create your views here.
def index(request):
    return render(request, 'pharmacist/index.html',{"data": getDrugs()})

def addDrug(request):
    form = AddDrugForm(request.POST)

    if(form.is_valid()):
        try:
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']

            newDrug = Drug(name = name,
                                 description = description)
            newDrug.save()
            print(newDrug)
            #print(newPatient.id)

            return render(request, "pharmacist/index.html", {
                "status": True,
                "message": "Drug added successfully",
                "data": getDrugs()
            })

        except:
            #print('not working')
            return render(request, "pharmacist/index.html", {
               "status": False,
               "message": "Action failed. Drug could not be added",
               "data": getDrugs()
            })
    
    else: 
        #print('horible')
        return render(request, "pharmacy/index.html",{"data": getDrugs()})

@api_view(['POST'])
def searchPrescription(request): 
    prescript = Prescription.objects.select_related('patient').get(prescription_id=request.data['text']) #.seletect_related('Patient')
    print(prescript)
    presItems = PrescriptionItem.objects.filter(prescription=prescript.id)

    presSer = PrescriptionResultSerializer(prescript) #PrescriptionSerializers(prescript)
    press = PrescriptionItemResultSerializer(presItems, many=True)
    print(presItems)
    return Response({"prescription": presSer.data, "drugs": press.data})
        