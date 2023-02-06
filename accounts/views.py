from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from django.contrib.auth.models import User

class UserListView(APIView):
    def get(self,request):
        data = User.objects.all()
        serializer_class = UserSerializer(data,many= True)
        return Response(
            serializer_class.data,
        )

class AddUserView(APIView):
    def post(self,request):
        serializer_class = UserSerializer(data = request.data)
        if(serializer_class.is_valid()):
            serializer_class.save()
            return Response(serializer_class.data)
        else:
            return Response(serializer_class.errors)