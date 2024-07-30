# middleware.py

from django.utils.deprecation import MiddlewareMixin
from django.conf import settings
from django.http import JsonResponse
from utility.utils import decode_jwt_token

#authentication checking for valid key
class JWTAuthenticationMiddleware(MiddlewareMixin):
    def process_request(self, request):
        
        if request.path == '/login/' or request.path =='/useregestration/':
            return None
        
        token = request.META.get('HTTP_AUTHORIZATION', None)
        if token is not None:
            try:
                token = token.split(' ')[1]
                payload = decode_jwt_token(token)
                if payload is None:
                    return JsonResponse({'error': 'Invalid token'}, status=401)
                request.user_id = payload['user_id']
                request.username = payload['username']
            except (IndexError, TypeError):
                return JsonResponse({'error': 'Token format is invalid'}, status=401)
        else:
            return JsonResponse({'error': 'Token missing'}, status=401)
