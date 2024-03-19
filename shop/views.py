from django.http import HttpResponse
import requests
from django.shortcuts import render


def greetings(request):
    return HttpResponse('Welcome to our shop!')


def cats(r):
    responser = requests.get('https://catfact.ninja/fact').json()
    print(responser)
    return HttpResponse(responser['fact'])



