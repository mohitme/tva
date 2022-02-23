from django.shortcuts import render
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_406_NOT_ACCEPTABLE,
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_500_INTERNAL_SERVER_ERROR,
)
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateDestroyAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from .serializers import (
    UserSerializer
)
from users.models import EndUser
# Create your views here.

class UserCreateListApi(APIView):
    def get(self, request):
        data = EndUser.objects.all()
        if data.count()>0:
            serializer = UserSerializer(data)
            return Response(serializer.data,status=HTTP_200_OK)
        else:
            return Response(status=HTTP_404_NOT_FOUND)
    def post(self, request):
        try:
            data = request.data
            serializer = UserSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(status=HTTP_201_CREATED)
        except Exception as e:
            return Response({"message": str(e)}, status=HTTP_500_INTERNAL_SERVER_ERROR)
    

class UserUpdateRetDelApi(APIView):
    def delete(self,pk):
        try:
            pk = self.kwargs['pk']
            row = EndUser.objects.filter(pk=pk)
            if row.count()>0:
                row.delete()
                return Response(status=HTTP_200_OK)
            else:
                return Response(status=HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(status=HTTP_500_INTERNAL_SERVER_ERROR)
    def get(self,pk):
        try:
            pk = self.kwargs['pk']
            row = User.objects.filter(pk=pk)
            if row.count()>0:
                serializer = UserSerializer(data=row)
                return Response(serializer.data,status=HTTP_200_OK)
            else:
                return Response(status=HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(status=HTTP_500_INTERNAL_SERVER_ERROR)
    def put(self, request):
        try:
            data = request.data
            news = EndUser.objects.get(id=data["id"])
            serializer = UserSerializer(news,data=n,partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(status=HTTP_200_OK)
        except EndUser.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"message": str(e)}, status=HTTP_500_INTERNAL_SERVER_ERROR)