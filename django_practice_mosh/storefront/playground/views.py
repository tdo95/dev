from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# View functions (request handler): request -> response

def calculate():
    x = 1
    y = 2
    return x

def say_hello(request):
    x = calculate()
    y = 2
    return render(request, 'hello.html', { 'name': 'Tee' })