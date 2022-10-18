from urllib import request
from django import http
import django
from django.http import HttpResponse
from django.shortcuts import render

from django.http import HttpResponse


# Create your views here.
def mostrar_inicio (request):
    return HttpResponse ("hola mundo")