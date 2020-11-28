from django.shortcuts import render
from django.views import View
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView


from users.tasks import send_notification_task
from .serializers import RegisterApiSerializer, LoginSerializer

User = get_user_model()


class RegisterApiView(APIView):
    def post(self, request):
        serializer = RegisterApiSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            if user:
                # TODO add send message with celery
                print("HELLO WORLD 1")
                send_notification_task.delay(user=user.id, seconds=10)
                print("HELLO WORLD 2")


                return Response(serializer.data, status=status.HTTP_201_CREATED)


class ActivationView(View):
    def get(self, request, activation_code):
        try:
            user = User.objects.get(activation_code=activation_code)
            user.is_active = True
            user.activation_code = ""
            user.save()
            return render(request, 'account/index.html', {})
        except User.DoesNotExist:
            return render(request, 'account/link_expired.html', {})


class LoginApiView(TokenObtainPairView):
    serializer_class = LoginSerializer

