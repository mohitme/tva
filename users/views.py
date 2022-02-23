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
            serializer = UserSerializer(data, many=True)
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
    def delete(self,request, pk):
        try:
            pk = self.kwargs['pk']
            row = EndUser.objects.filter(id=pk)
            if row.count()>0:
                row.delete()
                return Response(status=HTTP_200_OK)
            else:
                return Response(status=HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(status=HTTP_500_INTERNAL_SERVER_ERROR)
    def get(self, request, pk):
        try:
            pk = self.kwargs['pk']
            row = EndUser.objects.get(id=pk)
            serializer = UserSerializer(row)
            return Response(serializer.data,status=HTTP_200_OK)
        except EndUser.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"msg":e},status=HTTP_500_INTERNAL_SERVER_ERROR)
    def put(self, request, pk):
        try:
            pk = self.kwargs['pk']
            data = request.data
            user = EndUser.objects.get(id=pk)
            serializer = UserSerializer(user,data=data,partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(status=HTTP_200_OK)
        except EndUser.DoesNotExist:
            return Response(status=HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"message": str(e)}, status=HTTP_500_INTERNAL_SERVER_ERROR)