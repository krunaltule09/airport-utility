
from django.urls import path

from . import views

urlpatterns = [
    path('dashboard/gate',views.gateView,name='gate'),
    path('dashboard/trolley',views.trolleyView,name='trolley'),
    path('dashboard/baggage',views.baggageView,name='baggage'),
    path('dashboard/parking',views.parkingView,name='parking'),
    path('dashboard/home',views.homeView,name='home'),
    path('api/data/parking',views.parkingDataView,name='parkingData'),




]
