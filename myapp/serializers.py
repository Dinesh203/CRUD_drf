from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    """ UserSerializer model class """

    class Meta:
        """ User serializer Meta class """
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """ Create and return a new `User` instance, given the validated data."""
        password = validated_data['password']
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(password)
        user.save()
        return user
