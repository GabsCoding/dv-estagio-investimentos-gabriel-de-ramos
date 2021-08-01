from http.client import TOO_MANY_REQUESTS
from inspect import cleandoc
from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.fields import REGEX_TYPE
from rest_framework.response import Response
from rest_framework import status

from .serializers import ClientSerializer
from .models import Client
from api import serializers

@api_view(['GET'])
def list(request):
    api_urls = {
        'Create': '/new-client/',
        'Update': '/update-client/<str: key>',
        'Delete': '/delete-client/<str: key>'
    }

    clients = Client.objects.all()
    clients_serializer = ClientSerializer(clients, many=True)

    return Response({'overview': api_urls, 'data': clients_serializer.data})


@api_view(['POST'])
def create(request):
    client_serializer = ClientSerializer(data=request.data)

    if not client_serializer.is_valid(): return Response({'Response': 'NOT AVAILABLE'}, status=status.HTTP_406_NOT_ACCEPTABLE)
    
    client_serializer.save()
    return Response(client_serializer.data)


@api_view(['POST'])
def update(request, id):
    client = Client.objects.get(id=id)
    client_serializer = ClientSerializer(instance=client, data=request.data)

    if not client_serializer.is_valid(): return Response({"Response": "NOT FOUND"}, status=status.HTTP_404_NOT_FOUND)

    client_serializer.save()
    return Response(client_serializer.data)


@api_view(['DELETE'])
def delete(request, id):
    client = Client.objects.get(id=id)
    client.delete()

    return Response({'Response': 'DELETED'}, status=status.HTTP_200_OK)