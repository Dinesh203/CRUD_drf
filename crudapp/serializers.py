from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """Use model serializer"""

    class Meta:
        """ User serializer Meta class """
        model = User
        fields = ['id', 'username', 'email', 'password', 'date_of_birth']


