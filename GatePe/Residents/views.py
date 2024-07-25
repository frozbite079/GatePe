from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializer import *


###############################  ResidentView  ##########################################
class ResidentView(APIView):
    serializer_class = ResidentSerializer  
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = ResidentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            response = {"status": 200, "message": "Resident added"}
            return Response(response)
        return Response({"status": 400, "message": "Invalid data", "errors": serializer.errors})

    def get(self, request, *args, **kwargs):
        response = {'status': 200}
        residents = Resident.objects.all()
        serializer = ResidentSerializer(residents, many=True)
        response['data'] = serializer.data
        return Response(response)

    def delete(self, request, *args, **kwargs):
        response = {"status": 200}
        data = request.data
        try:
            resident = Resident.objects.get(id=data.get('id'))
            resident.delete()
            return Response({"status": 200, "message": "Resident deleted"})
        except Resident.DoesNotExist:
            return Response({"status": 404, "message": "Resident not found"})
        except Exception as e:
            print(e)
            return Response({"status": 400, "message": "An error occurred"})

    def patch(self, request, *args, **kwargs):
        response = {"status": 200}
        data = request.data
        try:
            resident = Resident.objects.get(id=data.get('id'))
            serializer = ResidentSerializer(resident, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                response['data'] = serializer.data
                return Response(response)
            return Response({"status": 400, "message": "Invalid data", "errors": serializer.errors})
        except Resident.DoesNotExist:
            return Response({"status": 404, "message": "Resident not found"})
        except Exception as e:
            print(e)
            return Response({"status": 400, "message": "An error occurred"})



############################## ServiceRequestView ################################################
class ServiceRequestView(APIView):
    serializer_class = ServiceRequestSerializer  
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = ServiceRequestSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            response = {"status": 200, "message": "Service request added"}
            return Response(response)
        return Response({"status": 400, "message": "Invalid data", "errors": serializer.errors})

    def get(self, request, *args, **kwargs):
        response = {'status': 200}
        service_requests = ServiceRequest.objects.all()
        serializer = ServiceRequestSerializer(service_requests, many=True)
        response['data'] = serializer.data
        return Response(response)

    def delete(self, request, *args, **kwargs):
        response = {"status": 200}
        data = request.data
        try:
            service_request = ServiceRequest.objects.get(id=data.get('id'))
            service_request.delete()
            return Response({"status": 200, "message": "Service request deleted"})
        except ServiceRequest.DoesNotExist:
            return Response({"status": 404, "message": "Service request not found"})
        except Exception as e:
            print(e)
            return Response({"status": 400, "message": "An error occurred"})

    def patch(self, request, *args, **kwargs):
        response = {"status": 200}
        data = request.data
        try:
            service_request = ServiceRequest.objects.get(id=data.get('id'))
            serializer = ServiceRequestSerializer(service_request, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                response['data'] = serializer.data
                return Response(response)
            return Response({"status": 400, "message": "Invalid data", "errors": serializer.errors})
        except ServiceRequest.DoesNotExist:
            return Response({"status": 404, "message": "Service request not found"})
        except Exception as e:
            print(e)
            return Response({"status": 400, "message": "An error occurred"})
        

############################################# ComplaintView ############################################
class ComplaintView(APIView):
    serializer_class = ComplaintSerializer  
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = ComplaintSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            response = {"status": 200, "message": "Complaint added"}
            return Response(response)
        return Response({"status": 400, "message": "Invalid data", "errors": serializer.errors})

    def get(self, request, *args, **kwargs):
        response = {'status': 200}
        complaints = Complaint.objects.all()
        serializer = ComplaintSerializer(complaints, many=True)
        response['data'] = serializer.data
        return Response(response)

    def delete(self, request, *args, **kwargs):
        response = {"status": 200}
        data = request.data
        try:
            complaint = Complaint.objects.get(id=data.get('id'))
            complaint.delete()
            return Response({"status": 200, "message": "Complaint deleted"})
        except Complaint.DoesNotExist:
            return Response({"status": 404, "message": "Complaint not found"})
        except Exception as e:
            print(e)
            return Response({"status": 400, "message": "An error occurred"})

    def patch(self, request, *args, **kwargs):
        response = {"status": 200}
        data = request.data
        try:
            complaint = Complaint.objects.get(id=data.get('id'))
            serializer = ComplaintSerializer(complaint, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                response['data'] = serializer.data
                return Response(response)
            return Response({"status": 400, "message": "Invalid data", "errors": serializer.errors})
        except Complaint.DoesNotExist:
            return Response({"status": 404, "message": "Complaint not found"})
        except Exception as e:
            print(e)
            return Response({"status": 400, "message": "An error occurred"})