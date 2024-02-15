from django.shortcuts import render
from .accountForm import LoginForm
from .models import Users

# Create your views here.

def index(request):
    return render(request, 'account/index.html',{})

def login(request):
    form = LoginForm(request.POST)

    if(form.is_valid()):
        #q = Users(full_name=form.cleaned_data('full_name'))
        print(form.cleaned_data['user_type'], 'test')
        print('good')
    else:
        form = LoginForm()
        print('not good')
    
    return render(request, "account/index.html", {"form": form})


