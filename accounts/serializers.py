from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import Token, RefreshToken

from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from .models import *
from django.contrib.auth import get_user_model

from datetime import timedelta

"""

TOken Serializer

"""

class CustomToken(Token):
    token_type = 'access'
    lifetime = timedelta(minutes=5)  # Set the token lifetime in seconds (5 minutes in this example)

    @classmethod
    def for_user(cls, user):
        token = super().for_user(user)
        token['uid'] = user.uid
        return token
    
    
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    default_error_messages = {
        'no_active_account': 'No active account found with the given email and password.',
        'other_problem': 'Bad Error'
    }
    email = serializers.EmailField(write_only=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove the 'username' field
        self.fields.pop('username')

    def validate(self, attrs):
        User = get_user_model()

        email = attrs.get('email')
        password = attrs.get('password')

        user = User.objects.get(email=email)

        if user.check_password(password):
            refresh = RefreshToken.for_user(user)
            access_token = CustomToken.for_user(user)
            return {
                'access': str(access_token),
                'refresh': str(refresh),
            }

        raise serializers.ValidationError('Invalid email or password')



""" 

User Serializer Class

"""

class UserSerializer(ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        User = get_user_model()
        model = User
        fields = ["first_name", "last_name", "email", "tel", "country", "date_of_birth", "username", "password"]

    def create(self, validated_data):
        data = validated_data
        User = get_user_model()
        user = User.objects.create(
            username=data["username"],
            first_name=data["first_name"],
            last_name=data["last_name"],
            email=data["email"],
            tel=data["tel"],
            country=data["country"],
            date_of_birth=data["date_of_birth"],
            password=data["password"]
        )
        
        print(user)
        
        refresh = RefreshToken.for_user(user)
        access = CustomToken.for_user(user)
        
        return {
            "refresh" : str(refresh),
            "access" : str(access)
        }