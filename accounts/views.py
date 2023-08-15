# from django.shortcuts import render, reverse, redirect, get_object_or_404
# from django.contrib.auth import get_user_model, login, logout, authenticate
# from django.http import JsonResponse

# User = get_user_model()


# def login_user(request):
#     if request.method == 'POST':
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#         user = authenticate(username=username, password=password)

#         if user:
#             login(request, user)
#             return JsonResponse({'message': 'Success', 'redirect': reverse('index')})
#         else:
#             return JsonResponse({'message': 'Invalid credentials'})

#     title = "Connexion"
#     context = {
#         "title": title
#     }
#     return JsonResponse({'html': render(request, "accounts/login.html", context).content.decode('utf-8')})


# def signup(request):
#     if request.method == 'POST':
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#         user = User.objects.create_user(username=username, password=password)

#         login(request, user)
#         return JsonResponse({'message': 'Success', 'redirect': reverse('index')})

#     title = "S'inscrire"
#     context = {
#         "title": title
#     }
#     return JsonResponse({'html': render(request, "accounts/signup.html", context).content.decode('utf-8')})


# def logout_user(request):
#     logout(request)
#     return JsonResponse({'message': 'Success', 'redirect': reverse('index')})


# Rest framework common import
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status

# TOKEN VIEW
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import Token, RefreshToken

# MODELS
# from .models import CustomUser
from django.contrib.auth import get_user_model

# Import Token Serializer
from .serializers import (
    MyTokenObtainPairSerializer,
    UserSerializer,
)



# Token generic getter view
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

# User register controller
class UserRegisterView(APIView):
    allowed_methods = ["POST, GET"]
    
    def get(self, request):
        return Response({"message": "Calling get"})
    
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        
        return Response(serializer.errors, status=400)





# Register controller
@api_view(['POST'])
def check_refresh_token_lifetime(token):
    refresh_token = RefreshToken(token)
    remaining_lifetime = refresh_token.lifetime.total_seconds()
    return remaining_lifetime
    
@api_view(["GET"])
def getRoutes(request):
    routes = [
        '/auth/token',
        '/auth/token/refresh',
        '/auth/token/verify',
        '/auth/token/life_time',
        # check_refresh_token_lifetime(token)
    ]

    return Response(routes)


@api_view(['POST'])
def getLifetime(request):
    refresh = request.POST.get("refresh")
    refresh_lifetime = check_refresh_token_lifetime(refresh)
    return Response(refresh_lifetime)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def pageFollowed(request):
    user = get_user_model()
    User = user.objects.get(username="zodiak")
    follow = User.pagefollowed_set.all()

    if follow:
        serializer = PageFollowedSerializer(follow, many=True)
        return Response(serializer.data)
    else :
        return Response(status=status.HTTP_400_BAD_REQUEST)
