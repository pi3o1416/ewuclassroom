from rest_framework import status
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from .serializers import CustomUserSerializer, MyTokenRefreshSerializer, MyTokenObtainPairSerializer


class ApiRoot(APIView):
    """
    Serve as a api root
    """
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        return Response({
            'register': reverse('account:user-registration', request=request),
            'token-obtain': reverse('account:token-obtain', request=request),
            'token-refresh': reverse('account:token-refresh', request=request),
        })


class Success(APIView):
    """
    Indicate success of api
    """

    def get(self, request):
        return Response(data={'hello': 'world'}, status=status.HTTP_200_OK)


class RegisterUser(APIView):
    """
    View to register a new User
    """
    permission_classes = (permissions.AllowAny,)
    serializer_class = CustomUserSerializer

    def post(self, request, format='json'):
        user = None
        serializer = self.serializer_class(data=request.data)
        print(request.data)
        if serializer.is_valid():
            try:
                user = serializer.save()
            except ValidationError as error:
                return Response(list(error), status=status.HTTP_200_OK)
            except IntegrityError as error:
                return Response(str(error), status=status.HTTP_200_OK)
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class MyTokenObtainPairView(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = MyTokenObtainPairSerializer
