from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('property-detail/<slug:slug>',views.propertyDetail,name='property_detail'),
    path('properties-list/',views.propertiesList,name='properties_list'),
]