from django.urls import path
from . import views



app_name = "accounts"
urlpatterns = [
    path('doctors/', views.doctors_list , name='doctors_list'),
    path('login/',views.login_user,name="login"),
    path('signUp/', views.signUp, name='signUp'),
    path('<slug:slug>/',views.doctors_detail),
]  