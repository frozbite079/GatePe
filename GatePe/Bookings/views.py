from django.shortcuts import render
from rest_framework.response import Response
from .models import *
from .serializer import *
from rest_framework.views import APIView

# Booking view
class BookingView(APIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    
    def get(self, request):
        response = {'status': 200}
        display_booking = Booking.objects.all()
        serializer = BookingSerializer(display_booking, many= True)
        response['data'] = serializer.data
        return Response(response)
    
    def post(self, request):
        data = request.data
        serializer = BookingSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            response = {"status":200, "message":"Data added"}
            return Response(response)
        return Response({"Status":400, "message":"Data not found"})
        
    def delete(self, request, ):
        
        response = {"status":200}
        data = request.data
        try:
            obj = Booking.objects.get(id=data.get('id'))
            obj.delete()
            return Response({"Status":200, "mesage":"Deleted"})
        except Exception as e:
            print(e)
        return Response({"Status":400, "message":"Data not found"})
    
     
    def patch(self, request, *args, **kwargs):
        
        response = {"status":200}
        data = request.data
        try:
            obj = data.objects.get(id=data.get('id'))
            serializer = BookingSerializer(obj, data=data, partial = True)
            if serializer.is_valid():
                serializer.save()
                response['data'] = serializer.data
                return Response(response)
            else:
                return Response(serializer.error)
        except Exception as e:
            print(e)
        return Response({'Status':400, "message":'Invalid id'})