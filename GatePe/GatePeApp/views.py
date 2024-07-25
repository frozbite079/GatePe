from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from .serializer import UserSerializer

class UserView(APIView):
    serializer_class = UserSerializer  

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            response = {"status": 200, "message": "User added"}
            return Response(response)
        return Response({"status": 400, "message": "Invalid data", "errors": serializer.errors})

    def get(self, request, *args, **kwargs):
        response = {'status': 200}
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        response['data'] = serializer.data
        return Response(response)

    def delete(self, request, *args, **kwargs):
        response = {"status": 200}
        data = request.data
        try:
            user = User.objects.get(id=data.get('id'))
            user.delete()
            return Response({"status": 200, "message": "User deleted"})
        except User.DoesNotExist:
            return Response({"status": 404, "message": "User not found"})
        except Exception as e:
            print(e)
            return Response({"status": 400, "message": "An error occurred"})

    def patch(self, request, *args, **kwargs):
        response = {"status": 200}
        data = request.data
        try:
            user = User.objects.get(id=data.get('id'))
            serializer = UserSerializer(user, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                response['data'] = serializer.data
                return Response(response)
            return Response({"status": 400, "message": "Invalid data", "errors": serializer.errors})
        except User.DoesNotExist:
            return Response({"status": 404, "message": "User not found"})
        except Exception as e:
            print(e)
            return Response({"status": 400, "message": "An error occurred"})
