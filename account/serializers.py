
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from django.contrib.auth import password_validation
from django.core.validators import validate_email
from .models import User


class CustomUserSerializer(serializers.ModelSerializer):
    """
    Serialize registration request and creates a new user
    """
    username = serializers.CharField(max_length=100)

    email = serializers.EmailField(
        max_length=100,
        required=True
    )

    password = serializers.CharField(
        max_length=100,
        min_length=8,
        write_only=True,
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password',
                  'first_name', 'last_name', 'role', 'dateOfBirth']

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        email = validated_data['email']
        print(email)
        isinstance = self.Meta.model(**validated_data)
        # validate email raise an exception if email is not valid
        validate_email(email)
        # validate password raise an exception if password does not meet all the criteria
        if password is not None:
            password_validation.validate_password(password)
            isinstance.set_password(password)
        isinstance.save()
        return isinstance


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['email'] = user.email
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        token['role'] = user.role
        token['dateOfBirth'] = str(user.dateOfBirth)
        return token


class MyTokenRefreshSerializer(TokenRefreshSerializer):
    pass
