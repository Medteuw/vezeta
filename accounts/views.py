from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Profile
from .forms import LoginForm, UserCreationForms
from django.contrib.auth import authenticate, login


def doctors_list(request):
    doctors = User.objects.all()
   
    return render(request,'accounts/doctors_list.html', {'doctors' : doctors,})

def doctors_detail(request, slug):
    doctors_detail = Profile.objects.get(slug=slug)
   
    return render(request,'accounts/doctors_detail.html', {'doctors_detail' : doctors_detail, })



def login_user(request):
    if request.method == 'POST':
        form = LoginForm()
        username = request.POST['username']
        password  = request.POST['password']
        user = authenticate(request,username= username,password = password)
        if user is not None:
            login(request,user)
            return redirect('accounts:doctors_list')
    else:
        form = LoginForm()

    
    return render(request,'accounts/login.html',{
        'form' : form
    })

def signUp(request):
    
    if request.method=='POST':
        form = UserCreationForms(request.POST)
        if form.is_valid:
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username,password = password)
            login(request,user)
            return redirect('accounts:doctors_list')

    else:
        form = UserCreationForms()

    return render(request,'accounts/signup.html',{
        'form' : form
    })