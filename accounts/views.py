from rest_framework import generics, permissions
from .models import User
from .serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken

class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ObtainAuthTokenView(generics.GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        user = User.objects.get(username=request.data['username'])
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })
