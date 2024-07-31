from django.shortcuts import render
from rest_framework.response import Response
from .models import *
from .serializer import *
from rest_framework.views import APIView

# Facility view
class FacilityView(APIView):
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer
    
    def get(self, request):
        
        try:
            if request.user_id:

                response = {'status': 200}
                display_facility = Facility.objects.all()
                serializer = FacilitySerializer(display_facility, many= True)
                response['data'] = serializer.data
                return Response(response)
            else:
                return Response({'Error':'Unauthorized'})
        except Exception as e:
            return Response({'error':str(e)})     


    def post(self, request):
        try:
            if request.user_id:

            
                data = request.data
                serializer = FacilitySerializer(data = data)
                if serializer.is_valid():
                    serializer.save()
                    response = {"status":200, "message":"Data added"}
                    return Response(response)
                return Response({"Status":400, "message":"Data not found"})
            else:
                return Response({'Error':'Unauthorized'})
        except Exception as e:
            return Response({'error':str(e)}) 
    
    def delete(self, request):
        try:
            if request.user_id:

                data = request.data
                try:
                    obj = Facility.objects.get(id=data.get('id'))
                    obj.delete()
                    return Response({"Status":200, "message":"Deleted"})
                except Exception as e:
                    print(e)
                return Response({"Status":400, "message":"Data not found"})
            else:
                return Response({'Error':'Unauthorized'}) 
        except Exception as e:
            return Response({'error':str(e)})    


     
    def patch(self, request):
        try:
            if request.user_id:

            
                response = {"status":200}
                data = request.data
                try:
                    obj = Facility.objects.get(id=data.get('id'))
                    serializer = FacilitySerializer(obj, data=data, partial = True)
                    if serializer.is_valid():
                        serializer.save()
                        response['data'] = serializer.data
                        return Response(response)
                    else:
                        return Response(serializer.error)
                except Exception as e:
                    print(e)
                return Response({'Status':400, "message":'Invalid id'})
            else:
                
                return Response({'Error':'Unauthorized'})
        except Exception as e:
            return Response({'error':str(e)})     


# Billing view
class BillingView(APIView):
    queryset = Billing.objects.all()
    serializer_class = BillingSerializer
    
    def get(self, request):
        try:
            if request.user_id:

                response = {'status': 200}
                display_billing = Billing.objects.all()
                serializer = BillingSerializer(display_billing, many= True)
                response['data'] = serializer.data
                return Response(response)
            else:
                return Response({'Error':'Unauthorized'}) 
        except Exception as e:
            return Response({'error':str(e)})    


    def post(self, request):
        try:

            if request.user_id:

                data = request.data
                serializer = BillingSerializer(data = data)
                if serializer.is_valid():
                    serializer.save()
                    response = {"status":200, "message":"Data added"}
                    return Response(response)
                return Response({"Status":400, "message":"Data not found"})
            else:
                return Response({'Error':'Unauthorized'}) 
        except Exception as e:
            return Response({'error':str(e)})     
    
    def delete(self, request, ):
        try:
            if request.user_id:

            
                response = {"status":200}
                data = request.data
                try:
                    obj = Billing.objects.get(id=data.get('id'))
                    obj.delete()
                    return Response({"Status":200, "mesage":"Deleted"})
                except Exception as e:
                    print(e)
                return Response({"Status":400, "message":"Data not found"})
            else:
                return Response({'Error':'Unauthorized'}) 
        except Exception as e:
            return Response({'error':str(e)})      


     
    def patch(self, request):
        try:
            if request.user_id:

                response = {"status":200}
                data = request.data
                try:
                    obj = Billing.objects.get(id=data.get('id'))
                    serializer = BillingSerializer(obj, data=data, partial = True)
                    if serializer.is_valid():
                        serializer.save()
                        response['data'] = serializer.data
                        return Response(response)
                    else:
                        return Response(serializer.error)
                except Exception as e:
                    print(e)
                return Response({'Status':400, "message":'Invalid id'})
            else:
                return Response({'Error':'Unauthorized'}) 
        except Exception as e:
            return Response({'error':str(e)})    


# Membership view
class MembershipView(APIView):
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer
    
    def get(self, request):
        try:
            if request.user_id:

                response = {'status': 200}
                display_membership = Membership.objects.all()
                serializer = MembershipSerializer(display_membership, many= True)
                response['data'] = serializer.data
                return Response(response)
            else:
                return Response({'Error':'Unauthorized'}) 
        except Exception as e:
            return Response({'error':str(e)})    

    def post(self, request):
        try:
            if request.user_id:

                data = request.data
                serializer = MembershipSerializer(data = data)
                if serializer.is_valid():
                    serializer.save()
                    response = {"status":200, "message":"Data added"}
                    return Response(response)
                return Response({"Status":400, "message":"Data not found"})
            else:
                return Response({'Error':'Unauthorized'}) 
        except Exception as e:
            return Response({'error':str(e)})   

    
    def delete(self, request, ):
        
        try:
            if request.user_id:

                response = {"status":200}
                data = request.data
                try:
                    obj = Membership.objects.get(id=data.get('id'))
                    obj.delete()
                    return Response({"Status":200, "mesage":"Deleted"})
                except Exception as e:
                    print(e)
                return Response({"Status":400, "message":"Data not found"})
            else:
                return Response({'Error':'Unauthorized'}) 
        except Exception as e:
            return Response({'error':str(e)})     

     
    def patch(self, request, *args, **kwargs):
        try:
            if request.user_id:

            
                response = {"status":200}
                data = request.data
                try:
                    obj = Membership.objects.get(id=data.get('id'))
                    serializer = MembershipSerializer(obj, data=data, partial = True)
                    if serializer.is_valid():
                        serializer.save()
                        response['data'] = serializer.data
                        return Response(response)
                    else:
                        return Response(serializer.error)
                except Exception as e:
                    print(e)
                return Response({'Status':400, "message":'Invalid id'})
            else:
                return Response({'Error':'Unauthorized'}) 
        except Exception as e:
            return Response({'error':str(e)})      
