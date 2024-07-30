from django.shortcuts import render

# views.py

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from utility.utils import generate_jwt_token
from UserRegestration.models import UserRegestration
import json
@csrf_exempt
def login_view(request):
    if request.method == 'POST':
           
        data = json.loads(request.body)
        
        username = data['username']
        password = data['password']
        print(username,password)
        try:
            user = UserRegestration.objects.get(username=username, password=password)
            token = generate_jwt_token(user)
            return JsonResponse({'token': token})
        except UserRegestration.DoesNotExist:
            return JsonResponse({'error': 'Invalid credentials'}, status=400)
@csrf_exempt
def demo_view(request):
    if request.user_id:
        return JsonResponse({'message': 'This is a protected view', 'user_id': request.user_id})
    return JsonResponse({'error': 'Unauthorized'}, status=401)
