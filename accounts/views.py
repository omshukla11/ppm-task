from rest_framework import (mixins, generics, status, permissions)
from rest_framework_simplejwt.tokens import RefreshToken
from django.http.response import HttpResponse, JsonResponse
from rest_framework.views import APIView
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import (mixins, generics, status, permissions)
from rest_framework.response import Response


from .serializers import *
from .utils import Util
# Create your views here.

class SignUp(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer1 = UserSerializer(data=request.data)
        if serializer1.is_valid():
            if(serializer1.data.get('is_admin')):
                user_data = serializer1.save_manager(serializer1.data)
            elif(serializer1.data.get('is_staff')):
                user_data = serializer1.save_staff(serializer1.data)
            else:
                return JsonResponse({'User has to be admin or staff'})
            refresh = RefreshToken.for_user(user_data)
            return JsonResponse({'status': 'created', 'refresh': str(refresh),'access': str(refresh.access_token)}, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer1.errors, status=status.HTTP_400_BAD_REQUEST)

class Login(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request':request})
        serializer.is_valid(raise_exception=True)
        return JsonResponse(serializer.validated_data, status=status.HTTP_200_OK)

class LogoutAPIView(generics.GenericAPIView):
    serializer_class = LogoutSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message':'Logged out successfully'},status=status.HTTP_204_NO_CONTENT)