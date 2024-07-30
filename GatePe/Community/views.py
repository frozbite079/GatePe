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

#########################  community post  ##################################

class CommunityPostView(APIView):
    serializer_class = CommunityPostSerializer  
    
    def get(self, request, *args, **kwargs):
        if request.user_id:
            response ={'status':200}
            display_communitypost =CommunityPost.objects.all()
        

        
            
        
            serializer=CommunityPostSerializer(display_communitypost,many=True)
            response['data']=serializer.data # type: ignore
            
            return Response(response)
                
        else:
            return Response({'Error':'Unauthorized'})   
    def post(self, request, *args, **kwargs):
        
        if request.user_id:
            data=request.data
            serializer=CommunityPostSerializer(data=data)
            if serializer.is_valid():
        
                serializer.save()
                response={"status":200,"message":"Community Post Data Added"}
                return Response(response)
            
            return Response(serializer.errors)
        else:
            return Response({'Error':'Unauthorized'})   
    def patch(self,request,*args, **kwargs):
    
        if request.user_id:
            response={'status':200}
            data=request.data
            try:
                obj=CommunityPost.objects.get(id=data.get('id'))
                serializer=CommunityPostSerializer(obj,data=data,partial=True)
                if serializer.is_valid():
                    serializer.save()
                    response['data']=serializer.data# type: ignore
                    return Response(response)
                else :
                    return Response(serializer.errors)
            except Exception as e:
                print(e)
            return Response({'status':400,'message':'invalid id'})
        else:
            return Response({'Error':'Unauthorized'})       
    def delete(self,request,*args, **kwargs):
        if request.user_id:
            response={'status':200}
            data=request.data 
            try:
                obj=CommunityPost.objects.get(id=data.get('id'))
                obj.delete()
                return Response({'status':200,'message':"Deleted"})
            except Exception as e:
                print(e)
            return Response({'status':400,'message':"Invalid id"})

        else:
            return Response({'Error':'Unauthorized'})   

#########################  notice  ##################################

class NoticeView(APIView):
    serializer_class = NoticeSerializer  
    
    def get(self, request, *args, **kwargs):
        if request.user_id:
            response ={'status':200}
            display_notice =Notice.objects.all()
        

        
            
        
            serializer=NoticeSerializer(display_notice,many=True)
            response['data']=serializer.data # type: ignore
            
            return Response(response)
        else:
            return Response({'Error':'Unauthorized'})   
                
    
    def post(self, request, *args, **kwargs):
        if request.user_id:
            data=request.data
            serializer=NoticeSerializer(data=data)
            if serializer.is_valid():
        
                serializer.save()
                response={"status":200,"message":"Notice Added"}
                return Response(response)
            
            return Response(serializer.errors)
        else:
            return Response({'Error':'Unauthorized'})   
        
    def patch(self,request,*args, **kwargs):
        
        if request.user_id:
            response={'status':200}
            data=request.data
            try:
                obj=Notice.objects.get(id=data.get('id'))
                serializer=NoticeSerializer(obj,data=data,partial=True)
                if serializer.is_valid():
                    serializer.save()
                    response['data']=serializer.data# type: ignore
                    return Response(response)
                else :
                    return Response(serializer.errors)
            except Exception as e:
                print(e)
            return Response({'status':400,'message':'invalid id'})
        else:
            return Response({'Error':'Unauthorized'})       
    def delete(self,request,*args, **kwargs):
        if request.user_id:
            response={'status':200}
            data=request.data 
            try:
                obj=Notice.objects.get(id=data.get('id'))
                obj.delete()
                return Response({'status':200,'message':"Deleted"})
            except Exception as e:
                print(e)
            return Response({'status':400,'message':"Invalid id"})

        else:
            return Response({'Error':'Unauthorized'})   



#########################  Survey  ##################################

class SurveyView(APIView):
    serializer_class = SurveySerializer  
    
    def get(self, request, *args, **kwargs):
        if request.user_id:
            response ={'status':200}
            display_survey =Survey.objects.all()
       

     
        
      
            serializer=SurveySerializer(display_survey,many=True)
            response['data']=serializer.data # type: ignore
            
            return Response(response)
        else:
            return Response({'Error':'Unauthorized'})   
                
    
    def post(self, request, *args, **kwargs):
        if request.user_id:
            data=request.data
            serializer=SurveySerializer(data=data)
            if serializer.is_valid():
        
                serializer.save()
                response={"status":200,"message":"Survey Added"}
                return Response(response)
            
            return Response(serializer.errors)
        else:
            return Response({'Error':'Unauthorized'})   
    
    def patch(self,request,*args, **kwargs):
        if request.user_id:
    
            response={'status':200}
            data=request.data
            try:
                obj=Notice.objects.get(id=data.get('id'))
                serializer=SurveySerializer(obj,data=data,partial=True)
                if serializer.is_valid():
                    serializer.save()
                    response['data']=serializer.data# type: ignore
                    return Response(response)
                else :
                    return Response(serializer.errors)
            except Exception as e:
                print(e)
            return Response({'status':400,'message':'invalid id'})
        else:
            return Response({'Error':'Unauthorized'})       
    def delete(self,request,*args, **kwargs):
        if request.user_id:
            response={'status':200}
            data=request.data 
            try:
                obj=Survey.objects.get(id=data.get('id'))
                obj.delete()
                return Response({'status':200,'message':"Deleted"})
            except Exception as e:
                print(e)
            return Response({'status':400,'message':"Invalid id"})

        else:
            return Response({'Error':'Unauthorized'})   



#########################  Surey Response  ##################################

class SurveyResponseView(APIView):
    serializer_class = SurveyResponseSerializer  
    
    def get(self, request, *args, **kwargs):
        if request.user_id:

            response ={'status':200}
            display_surveyresponse =SurveyResponse.objects.all()
        

        
            
        
            serializer=SurveyResponseSerializer(display_surveyresponse,many=True)
            response['data']=serializer.data # type: ignore
            
            return Response(response)
        
        else:
            return Response({'Error':'Unauthorized'})   
                
    
    def post(self, request, *args, **kwargs):
        if request.user_id:

            data=request.data
            serializer=SurveyResponseSerializer(data=data)
            if serializer.is_valid():
        
                serializer.save()
                response={"status":200,"message":"Survey Response Added"}
                return Response(response)
            
            return Response(serializer.errors)
        else:
            return Response({'Error':'Unauthorized'})   
        
        
    def patch(self,request,*args, **kwargs):
        if request.user_id:
    
            response={'status':200}
            data=request.data
            try:
                obj=SurveyResponse.objects.get(id=data.get('id'))
                serializer=SurveyResponseSerializer(obj,data=data,partial=True)
                if serializer.is_valid():
                    serializer.save()
                    response['data']=serializer.data# type: ignore
                    return Response(response)
                else :
                    return Response(serializer.errors)
            except Exception as e:
                print(e)
            return Response({'status':400,'message':'invalid id'})
        else:
            return Response({'Error':'Unauthorized'})    
    def delete(self,request,*args, **kwargs):
        if request.user_id:

            response={'status':200}
            data=request.data 
            try:
                obj=SurveyResponse.objects.get(id=data.get('id'))
                obj.delete()
                return Response({'status':200,'message':"Deleted"})
            except Exception as e:
                print(e)
            return Response({'status':400,'message':"Invalid id"})
        else:
            return Response({'Error':'Unauthorized'}) 




#########################  Feedback  ##################################

class FeedbackView(APIView):
    
    serializer_class = SurveyResponseSerializer  
    
    def get(self, request, *args, **kwargs):
        if request.user_id:

            response ={'status':200}
            display_feedback =Feedback.objects.all()
        

        
            
        
            serializer=FeedbackSerializer(display_feedback,many=True)
            response['data']=serializer.data # type: ignore
            
            return Response(response)
        else:
            return Response({'Error':'Unauthorized'}) 


    def post(self, request, *args, **kwargs):
        if request.user_id:

            data=request.data
            serializer=FeedbackSerializer(data=data)
            if serializer.is_valid():
        
                serializer.save()
                response={"status":200,"message":"Feedback Added"}
                return Response(response)
            
            return Response(serializer.errors)
        else:
            return Response({'Error':'Unauthorized'}) 


            
        
    def patch(self,request,*args, **kwargs):
        if request.user_id:

    
            response={'status':200}
            data=request.data
            try:
                obj=Feedback.objects.get(id=data.get('id'))
                serializer=FeedbackSerializer(obj,data=data,partial=True)
                if serializer.is_valid():
                    serializer.save()
                    response['data']=serializer.data# type: ignore
                    return Response(response)
                else :
                    return Response(serializer.errors)
            except Exception as e:
                print(e)
            return Response({'status':400,'message':'invalid id'})
        else:
            return Response({'Error':'Unauthorized'}) 
    
    def delete(self,request,*args, **kwargs):
        if request.user_id:

            response={'status':200}
            data=request.data 
            try:
                obj=Feedback.objects.get(id=data.get('id'))
                obj.delete()
                return Response({'status':200,'message':"Deleted"})
            except Exception as e:
                print(e)
            return Response({'status':400,'message':"Invalid id"})
        else:
            return Response({'Error':'Unauthorized'}) 
