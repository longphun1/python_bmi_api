from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import requests
# Create your views here.
url = "https://bmi.p.rapidapi.com/"

def index(request):
    return render(request, 'main/index.html', {
        "userData": Bmi.objects.all(), 
    })

def processBmi(request):
    form = request.POST
    errors = Bmi.objects.basic_validator(form)
    if len(errors) > 0:
        for key, val in errors.items():
            messages.error(request, val)
        return redirect('/accounts/profile')
    else:
        my_height = form['height']
        my_weight = form['weight']
        my_sex = form['sex']
        my_s = f'{my_sex}'
        my_age = form['age']
        my_waist = form['waist']
        payload = """{{\"weight\":{{\"value\":\"{my_weight}\",\"unit\":\"kg\"}},
                \"height\":{{\"value\":\"{my_height}\",\"unit\":\"cm\"}},
                \"sex\":\"{my_s}\",
                \"age\":\"{my_age}\",
                \"waist\":\"{my_waist}\"}}""".format(my_weight=my_weight, my_height=my_height, my_s=my_s, my_age=my_age, my_waist=my_waist)
        headers = {
            'x-rapidapi-host': "bmi.p.rapidapi.com",
            'x-rapidapi-key': "7cff70b7d1msh98d68cffc2f59cdp1ac70djsn2ec5c72d8ece",
            'content-type': "application/json",
            'accept': "application/json"
            }

        response = requests.request("POST", url, data=payload, headers=headers)

        bmi_status = response.json()['bmi']['status']
        bmi_risk = response.json()['bmi']['risk']
        bmi_ideal = response.json()['ideal_weight']
        Bmi.objects.create(user=form['user'], weight=form['weight'], height=form['height'], sex=form['sex'], age=form['age'], waist=form['waist'], status=bmi_status, risk=bmi_risk, ideal=bmi_ideal)
        return redirect('/accounts/profile/')

def editBmi(request, data_id):
    return render (request, 'main/edit.html', {
        "data": Bmi.objects.get(id=data_id)
    })

def processEdit(request, data_id):
    form = request.POST
    errors = Bmi.objects.basic_validator(form)
    if len(errors) > 0:
        for key, val in errors.items():
            messages.error(request, val)
        return redirect(f"/editBmi/{data_id}")
    else:
        my_weight = form['weight']
        my_height = form['height']
        my_sex = form['sex']
        my_s = f'{my_sex}'
        my_age = form['age']
        my_waist = form['waist']
        payload = """{{\"weight\":{{\"value\":\"{my_weight}\",\"unit\":\"kg\"}},
                \"height\":{{\"value\":\"{my_height}\",\"unit\":\"cm\"}},
                \"sex\":\"{my_s}\",
                \"age\":\"{my_age}\",
                \"waist\":\"{my_waist}\"}}""".format(my_weight=my_weight, my_height=my_height, my_s=my_s, my_age=my_age, my_waist=my_waist)
        headers = {
            'x-rapidapi-host': "bmi.p.rapidapi.com",
            'x-rapidapi-key': "7cff70b7d1msh98d68cffc2f59cdp1ac70djsn2ec5c72d8ece",
            'content-type': "application/json",
            'accept': "application/json"
            }

        response = requests.request("POST", url, data=payload, headers=headers)
        update = Bmi.objects.get(id=data_id)
        update.height=form['height']
        update.weight=form['weight']
        update.age=form['age']
        update.waist=form['waist']
        update.sex=form['sex']
        update.status=response.json()['bmi']['status']
        update.risk=response.json()['bmi']['risk']
        update.ideal=response.json()['ideal_weight']
        update.save()
        return redirect('/accounts/profile/')

def deleteBmi(request, data_id):
    Bmi.objects.get(id=data_id).delete()
    return redirect('/accounts/profile/')

