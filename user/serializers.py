from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """ A serializer class for the User model """
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'username',
                  'password', 'is_active', 'is_superuser')