from django.shortcuts import render, redirect
from .accountForm import LoginForm
from .models import Users
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .accountSerializer import UsersSerializers

# Create your views here.

def index(request):
    return render(request, 'account/index.html',{})

def login(request):
    form = LoginForm(request.POST)

    if(form.is_valid()):
        #q = Users(full_name=form.cleaned_data('full_name'))
        try : 
            user = Users.objects.get(email=form.cleaned_data['email'],
                                 password=form.cleaned_data['password'],
                                 user_type=form.cleaned_data['user_type'])
            #print(form.cleaned_data['user_type'], 'test')
            if form.cleaned_data['user_type'] == "Doctor":
                return redirect("/doctor/")
            else :
                return redirect("/pharmacy/")
        except:
            return render(request, "account/index.html", {
                "status": False,
                "message": "Login  failed. Wrong email & password",
            })
    else:
        form = LoginForm()
        print('not good')
    
    return render(request, "account/index.html", {"form": form})

#This is just for testing Django rest framework
@api_view(['GET'])
def getUsers(request):
        allUsers = Users.objects.all()
        serializ = UsersSerializers(allUsers, many=True)
        '''users = {
            'name': 'victor ijoni',
            'age': 20
        }'''
        return Response(serializ.data)

@api_view(['POST'])
def addUser(request):
    print(request.data['full_name'])
    serializ = UsersSerializers(data = request.data)
    if serializ.is_valid() : 
        #serializ.save()
        print(serializ.data)
        return Response(serializ.data)
    return Response()
    
    
