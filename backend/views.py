from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer
from rest_framework import status


@api_view(['POST'])
def login(request):
    return Response({})


@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(
        data={"username": request.data['email'], "email": request.data['email'], "password": request.data['password']})
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=request.data['email'])
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response({'token': token.key}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def test_token(request):
    return Response({})
