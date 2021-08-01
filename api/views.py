from http.client import TOO_MANY_REQUESTS
from inspect import cleandoc
from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ClientSerializer
from .models import Client

@api_view(['GET'])
def list(request):
    api_urls = {
        'Create': '/new-client/',
        'Update': '/update-client/<str: key>',
        'Delete': '/delete-client/<str: key>'
    }

    clients = Client.objects.all()
    clients_serializer = ClientSerializer(clients, many=True)

    #return Response({'overview': api_urls, 'data': client_serializer.data})
    return Response(clients_serializer.data)

# @api_view(['POST'])
# def create(request):
#     api_urls = {
#         'List': '/',
#         'Create': '/new-client/',
#         'Update': '/update-client/<str: key>',
#         'Delete': '/delete-client/<str: key>'
#     }

#     return Response(api_urls)

# @api_view(['POST'])
# def update(request):
#     api_urls = {
#         'List': '/',
#         'Create': '/new-client/',
#         'Update': '/update-client/<str: key>',
#         'Delete': '/delete-client/<str: key>'
#     }

#     return Response(api_urls)