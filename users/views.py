from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema

from users.models import User
from users.serializers import UserPrivateSerializer, UserPublicSerializer, UserRegisterSerializer

class UsersView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserPublicSerializer(users, many=True)
        return Response(serializer.data)

class UsersDetailView(APIView):
    def get(self, request, pk):
        user = User.objects.get(id=pk)
        serializer = UserPublicSerializer(user)
        return Response(serializer.data)

class UsersMeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = User.objects.get(id=request.user.id)
        serializer = UserPrivateSerializer(user)
        return Response(serializer.data)
    
    @extend_schema(request=UserPrivateSerializer, responses=UserPrivateSerializer)
    def put(self, request):
        serializer = UserPrivateSerializer(request.user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class UsersRegisterView(APIView):
    @extend_schema(request=UserRegisterSerializer, responses=UserRegisterSerializer)
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
