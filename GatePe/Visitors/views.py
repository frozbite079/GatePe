from django.shortcuts import render
from .models import *
from .serializer import *
from urllib import response
from django import views
from django.http import JsonResponse
from django.shortcuts import render,redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.

class VisitorView(APIView):
    serializer_class = VisitorSerializer  
    
    def get(self, request, *args, **kwargs):
        response ={'status':200}
        display_visitor =Visitor.objects.all()
       

     
        
        # if i.role=="Player":
        serializer=VisitorSerializer(display_visitor,many=True)
        response['data']=serializer.data # type: ignore
        
        return Response(response)
              
    
    def post(self, request, *args, **kwargs):
        data=request.data
        serializer=VisitorSerializer(data=data)
        if serializer.is_valid():
      
            serializer.save()
            response={"status":200,"message":"Visitor Data Added"}
            return Response(response)
        
        return Response(serializer.errors)
    
    def patch(self,request,*args, **kwargs):
    
        response={'status':200}
        data=request.data
        try:
            obj=Visitor.objects.get(id=data.get('id'))
            serializer=VisitorSerializer(obj,data=data,partial=True)
            if serializer.is_valid():
                serializer.save()
                response['data']=serializer.data# type: ignore
                return Response(response)
            else :
                return Response(serializer.errors)
        except Exception as e:
            print(e)
        return Response({'status':400,'message':'invalid id'})
        
    def delete(self,request,*args, **kwargs):
        response={'status':200}
        data=request.data 
        try:
            obj=Visitor.objects.get(id=data.get('id'))
            obj.delete()
            return Response({'status':200,'message':"Deleted"})
        except Exception as e:
            print(e)
        return Response({'status':400,'message':"Invalid id"})
