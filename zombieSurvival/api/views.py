from django.shortcuts import render

import json

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from api.models import Survivor
from api.serializers import SurvivorSerializer, Survivor_LocationSerializer



@csrf_exempt
def survivor_create(request):
    """
    Api to get List of all survivals and create a new survivor 
    """
    
    if request.method == 'GET':
        survivor = Survivor.objects.all()
        serializer = SurvivorSerializer(survivor, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        name = data['name']
        age = data['age']
        gender = data['gender']
        latitude = data['latitude']
        longitude = data['longitude']
        is_infected = data['is_infected']
        count_report = 0
        if (is_infected == False):
            is_infected = False
        else:
            is_infected = True
            
        survivor_serializer = SurvivorSerializer(data=data)
        
        try:
            if survivor_serializer.is_valid():
                s = survivor_serializer.save()
                return JsonResponse(survivor_serializer.data, status=200)
                
        except KeyError:
            return HttpResponse(json.dumps({"error": "Data isn't valid"}, status=404))
        
        

@csrf_exempt
def survivor_update(request, pk):
    """
    Api to Retrieve , update survivor  
    """
    
    try :
        survivor = Survivor.objects.get(pk=pk)
        
    except Survivor.DoesNotExist:
        return HttpResponse(json.dumps({"error": "Survivor Does not exists "}, status=404))
    
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = Survivor_LocationSerializer(survivor, data=data)
        if serializer.is_valid():
            serializer.save()
            s_serializer = SurvivorSerializer(survivor)
            return JsonResponse(s_serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)
    
    
def infected_survivors_report(request):
    infected = 0.0
    
    if request.method == 'GET':
        survivor = Survivor.objects.all()
        for s in survivor:
            if s.is_infected:
                infected += 1
                
        percent_of_infected = (infected/survivor.count())*100
        return HttpResponse(json.dumps({"percentage of infected people": percent_of_infected}), status=200)
    
    
def no_infected_survivor_report(request):
    no_infected = 0.0
    
    if request.method == 'GET':
        survivor = Survivor.objects.all()
        for s in survivor:
            if not (s.is_infected):
                no_infected += 1
                
        percentage_of_non_infected = (no_infected/survivor.count())*100
        return HttpResponse(json.dumps({"Percentage of no infected persons": percentage_of_non_infected}), status=200)
        
        
            
            

