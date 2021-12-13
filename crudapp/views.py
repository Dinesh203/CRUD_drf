from crudapp.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse, HttpResponse, Http404
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated


# Create your views here.


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': "Hello, Dinesh"}
        return Response(content)


class UserDetail(APIView):
    """ List , retrieve, update, delete users
    """
    def get_user_model(self, request, pk):
        """ GET and POST users """
        if request.method == "GET":
            return User.objects.filter(pk=pk)
        elif request.method == "POST":
            pass

    def get_user_serializerts(self, request, pk):
        """" GET and POST """
        if request.method == "GET":
            return UserSerializer(self.get_user_model(request, pk), many=True)
        elif request.method == "POST":
            return UserSerializer(data=request.data)

    # def get_all(self, request):
    #     user = User.objects.all()
    #     serializers = UserSerializer(user, data=User.data, many=True)
    #     return Response(serializers.data)

    def get(self, request, pk):
        print(pk)
        serializers = self.get_user_serializerts(request, pk)
        return Response(serializers.data)

    def post(self, request):
        serializer = self.get_user_serializerts(request)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        user_id = self.get_user_serializerts(request, pk)
        serializer = UserSerializer(user_id, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user_id = self.get_user_model(pk)
        user_id.delete()
        return Response(status=status.HTTP_200_OK)
