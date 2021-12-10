from django.shortcuts import render
from crudapp.serializers import UserSerializer
from rest_framework.parsers import JSONParser
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView

# Create your views here.


# class Apiviews()