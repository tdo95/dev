from django.urls import path
# This allows us to reference our view function
from . import views

#URL Configuration module
urlpatterns = [
    path('hello/', views.say_hello)

]