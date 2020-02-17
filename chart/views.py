from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
import random,requests
from datetime import datetime
from .models import gasdb,phdb,sounddb
from django.views.generic import View
from firebase import firebase
import random
from datetime import datetime

def gateView(request):
    return render(request,"gate.html",{})

def trolleyView(request):
    return render(request,"trolley.html",{})

def baggageView(request):
    return render(request,"baggage.html",{})

def parkingView(request):
    return render(request,"parking.html",{})

def homeView(request):
    return render(request,"home.html",{})



def parkingDataView(request):

    app=firebase.FirebaseApplication('https://airport-22afd.firebaseio.com')
    
    result=app.get('/parking',None)
    print(result)
    cars=int(result['cars'])
    print(type(cars))
    cars=cars+(cars%10)+10
    context={
        "cars":cars,
        "timeCreated":result['time']
    }
    # context={
    #     "cars":random.randint(1,200),
    #     "timeCreated":str(datetime.now())[11:19]

    # }

    return JsonResponse(context)










