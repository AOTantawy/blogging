from django.shortcuts import render
from django.http import HttpResponse
from .viewsDir.userViews import *

# Create your views here.
def index(request):
    return HttpResponse('Hello World !!')