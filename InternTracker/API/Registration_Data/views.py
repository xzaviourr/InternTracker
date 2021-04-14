from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import registration
from .serializers import Registration_Data_Serializeer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

@api_view(["GET","POST"])
def show_list(request):
    if request.method=="GET":
        data=registration.objects.all()  #gives all the data stored in the model.py
        #But this data is in Python format.To convert it into JSON format,we make a serializer
        serializers=Registration_Data_Serializeer(data,many=True) #converts Python to JSON
        return Response(serializers.data)
    elif request.method=="POST":
        serializers=Registration_Data_Serializeer(data=request.data) #Fetching data from the API
        if serializers.is_valid():  #checking whether data is fetched as per fields
            serializers.save()      #saving into database if valid     
            return Response(serializers.data,status=status.HTTP_201_CREATED)      
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)