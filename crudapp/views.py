
from crudapp.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse, HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from django.contrib.auth.models import User


# Create your views here.


class UserDetail(APIView):
    """ List , retrieve, update, delete users
    """

    def get_user_model(self, request):
        """ GET and POST users """
        if request.method == "GET":
            return User.objects.all()
        elif request.method == "POST":
            pass

    def get_user_serializerts(self, request):
        """" GET and POST """
        if request.method == "GET":
            return UserSerializer(self.get_user_model(request), many=True)
        elif request.method == "POST":
            return UserSerializer(data=request.data)

    def get(self, request):
        serializers = self.get_user_serializerts(request)
        return Response(serializers.data)

    def post(self, request):
        serializer = self.get_user_serializerts(request)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserUpdate(APIView):
    """
    Update and delete users
    """
    def get_object_id(self, pk):
        """ Get user id """
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        user_id = self.get_object_id(pk)
        serializer = UserSerializer(user_id, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user_id = self.get_object_id(pk)
        user_id.delete()
        return Response(status=status.HTTP_200_OK)

