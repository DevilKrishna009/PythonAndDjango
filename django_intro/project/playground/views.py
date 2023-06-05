from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def test_hello_name(request, name):
    return HttpResponse(f"Hello,{name}")
