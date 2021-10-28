from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])

def imageProcessing(request):

    if request.method == 'GET':
        return Response('hello')

    elif request.method == 'POST':
        return Response(request.body)