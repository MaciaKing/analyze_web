from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.conf import settings
from cyberintelligence.classes.virus_total import VirusTotal

# Validate that the api is working
def index(request):
    response={
        "response": "working"
    }
    return JsonResponse(response)

def prueba_vt(request):
    vt = VirusTotal(settings.VIRUS_TOTAL_API_KEY)
    vt.make_query()
    response={
        "virus_total_api_key": settings.VIRUS_TOTAL_API_KEY
    }
    return JsonResponse(response)