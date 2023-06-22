from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Pais
from .serializers import PaisSerializador

@api_view(['GET','POST'])
def pais(request):
    print(request)

    if request.method == 'GET':
        paises = Pais.objects.all()
        serializer = PaisSerializador(paises,many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        print(request.data)
        serializer = PaisSerializador(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
def index(request):
    if request.method == 'GET':
        return HttpResponse('Index')