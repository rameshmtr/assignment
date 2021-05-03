from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.core.exceptions import ValidationError


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def create(self, request):

        username = request.data.get('username')
        password = request.data.get('password')

        if username and password:

            user = User.objects.create(
                username=username,
            )
        
            user.set_password(password)
            user.save()
        
        else:

            raise ValidationError('Username and Password Required')


        token, created = Token.objects.get_or_create(user=user)

        return Response({
            'access_token': token.key,
        })
        