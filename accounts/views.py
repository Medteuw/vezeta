from django.shortcuts import render
from django.contrib.auth.models import User



def app(request):
    doctors = User.objects.all()
   
    return render(request,'accounts/doctors_list.html', {'doctors' : doctors,})
