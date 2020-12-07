from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model()

class RegisterApiSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        min_length=6, required=True,
        write_only=True)
    password_confirmation = serializers.CharField(
        min_length=6, required=True,
        write_only=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'password_confirmation')

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("User with given email already exists!")
        return value

    def validate(self, attrs):
        password = attrs.get('password')
        password_confirmation = attrs.pop('password_confirmation')

        if password != password_confirmation:
            raise serializers.ValidationError("Passwords don't match!")
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class LoginSerializer(TokenObtainPairSerializer):
    password = serializers.CharField(min_length=6, write_only=True)

    def validate_email(self, value):
        if not User.objects.filter(email=value).exists():
            raise serializers.ValidationError("""
            User with this email was not found: Please type in valid email!
            """)
        return value

    def validate(self, attrs):
        email = attrs.get('email')

        password = attrs.pop('password')
        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError('Not Found')

        user = authenticate(username=email, password=password)
        if user and user.is_active:
            refresh = self.get_token(user)

            attrs['refresh'] = str(refresh)
            attrs['access'] = str(refresh.access_token)

        return attrs
    
class ChangePasswordSerializer(serializers.Serializer):

    model = User

    old_password = serializers.CharField(
        min_length=6, required=True,
        write_only=True)
    new_password = serializers.CharField(
        min_length=6, required=True,
        write_only=True)
