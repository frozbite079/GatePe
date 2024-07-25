from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializer import *

class EstateView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = EstateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            response = {"status": 200, "message": "Estate added"}
            return Response(response)
        return Response({"status": 400, "message": "Invalid data", "errors": serializer.errors})

    def get(self, request, *args, **kwargs):
        response = {'status': 200}
        estates = Estate.objects.all()
        serializer = EstateSerializer(estates, many=True)
        response['data'] = serializer.data
        return Response(response)

    def delete(self, request, *args, **kwargs):
        response = {"status": 200}
        data = request.data
        try:
            estate = Estate.objects.get(id=data.get('id'))
            estate.delete()
            return Response({"status": 200, "message": "Estate deleted"})
        except Estate.DoesNotExist:
            return Response({"status": 404, "message": "Estate not found"})
        except Exception as e:
            print(e)
            return Response({"status": 400, "message": "An error occurred"})

    def patch(self, request, *args, **kwargs):
        response = {"status": 200}
        data = request.data
        try:
            estate = Estate.objects.get(id=data.get('id'))
            serializer = EstateSerializer(estate, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                response['data'] = serializer.data
                return Response(response)
            return Response({"status": 400, "message": "Invalid data", "errors": serializer.errors})
        except Estate.DoesNotExist:
            return Response({"status": 404, "message": "Estate not found"})
        except Exception as e:
            print(e)
            return Response({"status": 400, "message": "An error occurred"})
        

############################# Property Views #############################
class PropertyView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = PropertySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            response = {"status": 200, "message": "Property added"}
            return Response(response)
        return Response({"status": 400, "message": "Invalid data", "errors": serializer.errors})

    def get(self, request, *args, **kwargs):
        response = {'status': 200}
        properties = Property.objects.all()
        serializer = PropertySerializer(properties, many=True)
        response['data'] = serializer.data
        return Response(response)

    def delete(self, request, *args, **kwargs):
        response = {"status": 200}
        data = request.data
        try:
            property = Property.objects.get(id=data.get('id'))
            property.delete()
            return Response({"status": 200, "message": "Property deleted"})
        except Property.DoesNotExist:
            return Response({"status": 404, "message": "Property not found"})
        except Exception as e:
            print(e)
            return Response({"status": 400, "message": "An error occurred"})

    def patch(self, request, *args, **kwargs):
        response = {"status": 200}
        data = request.data
        try:
            property = Property.objects.get(id=data.get('id'))
            serializer = PropertySerializer(property, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                response['data'] = serializer.data
                return Response(response)
            return Response({"status": 400, "message": "Invalid data", "errors": serializer.errors})
        except Property.DoesNotExist:
            return Response({"status": 404, "message": "Property not found"})
        except Exception as e:
            print(e)
            return Response({"status": 400, "message": "An error occurred"})
