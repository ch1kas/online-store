from django.shortcuts import render
from django.views import View
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import permissions
# from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny


from users.tasks import send_notification_task
from .serializers import RegisterApiSerializer, LoginSerializer, ChangePasswordSerializer

User = get_user_model()

'''
Api View for registering. Anyone is allowed to register
'''

class RegisterApiView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterApiSerializer(data=request.data)
        # checking for validation
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            if user:
                # print("HELLO WORLD 1")
                # sending confirmation email using celery (async)
                send_notification_task.delay(user=user.id, seconds=10)
                # print("HELLO WORLD 2")


                return Response(serializer.data, status=status.HTTP_201_CREATED)


'''
View for activating an account
'''
class ActivationView(View):
    def get(self, request, activation_code):
        try:
            # If user with such activation code exists we label that user as an active one and get rid of activation code
            user = User.objects.get(activation_code=activation_code)
            user.is_active = True
            user.activation_code = ""
            user.save()
            return render(request, 'account/index.html', {})
        except User.DoesNotExist:
            return render(request, 'account/link_expired.html', {})


'''
View for loggin in
'''
class LoginApiView(TokenObtainPairView):
    serializer_class = LoginSerializer


"""

"""
class PasswordChangeApiView(APIView):
    """
    An endpoint for changing password.
    """
    model = User
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = ChangePasswordSerializer

    def get_object(self, queryset=None):
        return self.request.user

    def put(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = ChangePasswordSerializer(data=request.data)
        print(self.object.password)

        if serializer.is_valid():
            # Check old password
            old_password = serializer.data.get("old_password")
            print(self.object.check_password(old_password))
            if not self.object.check_password(old_password):
                return Response({"old_password": ["Wrong password."]},
                                status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)