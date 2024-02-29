from django.shortcuts import render
from .addDrugForm import AddDrugForm
from .models import Drug



# Create your views here.
def index(request):
    return render(request, 'pharmacist/index.html',{})

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
                "data": newDrug.id
            })

        except:
            #print('not working')
            return render(request, "pharmacist/index.html", {
               "status": False,
               "message": "Action failed. Drug could not be added",
            })
    
    else: 
        #print('horible')
        return render(request, "pharmacy/index.html",{})
    