from rest_framework import serializers
from .models import User
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken, TokenError


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password', 'is_staff', 'is_admin']
    
    def save_manager(self, validated_data):
        user = User.objects.create_superuser( 
                                password=validated_data.get('password'), 
                                email=validated_data.get('email'),
                                )
        user.save()
        return user
    
    def save_staff(self, validated_data):
        user = User.objects.create_staffuser( 
                                password=validated_data.get('password'), 
                                email=validated_data.get('email'),
                                )
        user.save()
        return user

class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=3)
    password = serializers.CharField(max_length=68, min_length=3)
    token = serializers.CharField(max_length=68, min_length=8, read_only=True)

    class Meta:
        model=User
        fields = ['email', 'password', 'token']

    def validate(self, attrs):

        email = attrs.get('email','')
        password = attrs.get('password', '')

        filtered_user_by_email = User.objects.filter(email=email)
        auth_user = auth.authenticate(email=email, password=password)

        if not auth_user:
            raise AuthenticationFailed("Invalid credentials, try again")
        if not auth_user.is_active:
            raise AuthenticationFailed("Account not active! Activate with the email link sent")

        tokens = RefreshToken.for_user(user=auth_user)
        return {
            'email': auth_user.email,
            'admin': auth_user.is_admin,
            'staff': auth_user.is_staff,
            'refresh': str(tokens),
            'access': str(tokens.access_token)
        }

class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    default_error_message = {
        'bad_token': ('Token is expired or invalid')
    }

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):

        try:
            RefreshToken(self.token).blacklist()

        except TokenError:
            self.fail('bad_token')

