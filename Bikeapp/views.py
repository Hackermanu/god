from django.shortcuts import render,redirect
from Bikeapp.models import Bike  

def reg_page(request):
    return render(request,'reg_page.html')
def reg_details(request):
    dict=request.GET
    name=dict['bn']
    company=dict['bc']
    milage=dict['bm']
    price=dict['bp']
    obj=Bike()
    obj.bike_name=name
    obj.bike_company=company
    obj.bike_milage=milage
    obj.bike_price=price
    obj.save()
    return redirect('/Bikeapp/reg_page')
def records(request):
    object=Bike.objects.all()
    return render(request,'all_records.html',{'obj': object})
def company_page(request):
    return render(request,'company.html')
def display_cmpny(request):
    dict=request.GET
    name=dict['nm']
    object=Bike.objects.filter(bike_company=name)
    return render(request,'all_records.html',{'obj': object})
def price_data(request):
    return render(request,'price.html')
def search_result(request):
    dict=request.GET
    price=dict['pr']
    object=Bike.objects.filter(bike_price=price)
    return render(request,'all_records.html',{'obj':object})
