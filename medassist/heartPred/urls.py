from django.urls import path
from . import views

urlpatterns = [
    path('form/', views.heart_form, name='heart_form'), 
    path('predict/', views.heart_predict, name='heart_predict'), 

 ]
