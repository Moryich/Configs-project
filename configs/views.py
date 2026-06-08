from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema

from configs.models import Config
from configs.serializers import ConfigSerializer

class ConfigsView(APIView):
    def get(self, request):
        configs = Config.objects.all()
        serializer = ConfigSerializer(configs, many=True)
        return Response(serializer.data)

    @extend_schema(request=ConfigSerializer, responses=ConfigSerializer)
    def post(self, request):
        serializer = ConfigSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ConfigDetailView(APIView):
    def get(self, request, pk):
        config = Config.objects.get(id=pk)
        serializer = ConfigSerializer(config)
        return Response(serializer.data)

    @extend_schema(request=ConfigSerializer, responses=ConfigSerializer)
    def put(self, request, pk):
        config = Config.objects.get(id=pk)
        serializer = ConfigSerializer(config, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        config = Config.objects.get(id=pk)
        config.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

