from django.urls import path
from . import views


app_name = "accounts"
urlpatterns = [
    path('doctors/', views.app , name='doctors'),
]