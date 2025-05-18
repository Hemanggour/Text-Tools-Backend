from django.contrib.auth import login, logout
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from account.models import ApikeyModel, UserModel
from account.serializers import ApikeySerializer, UserSerializer

# Create your views here.


class LoginView(APIView):
    class PostSerializer(serializers.Serializer):
        email = serializers.EmailField(required=True)
        password = serializers.CharField(required=True)

    def post(self, *args, **kwargs):
        serializer = self.PostSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data.get("email")
        password = serializer.validated_data.get("password")

        try:
            user = UserModel.objects.get(email=email)
            if not user.check_password(password):
                raise UserModel.DoesNotExist
        except UserModel.DoesNotExist:
            return Response({"message": "Unauthorized user"}, status=401)

        login(self.request, user=user)
        return Response(UserSerializer(user).data, status=200)


class RegisterView(APIView):
    class PostSerializer(serializers.Serializer):
        email = serializers.EmailField(required=True)
        password = serializers.CharField(required=True)

    def post(self, *args, **kwargs):
        serializer = self.PostSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data.get("email")
        password = serializer.validated_data.get("password")

        if UserModel.objects.filter(email=email).exists():
            return Response({"message": "Email already exists"}, status=403)

        user_serializer = UserSerializer(data={"email": email, "password": password})
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()

        login(self.request, user=user)

        return Response(UserSerializer(user).data, status=201)


class ApikeyView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return Response({"message": "Unauthorized access"}, status=403)

        try:
            user_obj = UserModel.objects.get(pk=self.request.user.pk)
        except UserModel.DoesNotExist:
            return Response({"message": "User Does Not exist"}, status=403)

        try:
            api_key_obj = ApikeyModel.objects.get(user=user_obj)
        except ApikeyModel.DoesNotExist:
            return Response({"message": "API Key does not exist"}, status=404)

        serializer = ApikeySerializer(api_key_obj)
        return Response(serializer.data, status=200)

    def post(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return Response({"message": "Unauthorized access"}, status=403)

        try:
            user_obj = UserModel.objects.get(pk=self.request.user.pk)
        except UserModel.DoesNotExist:
            return Response({"message": "User Does Not exist"}, status=403)

        if ApikeyModel.objects.filter(user=user_obj).exists():
            return Response({"message": "API Key already exists"}, status=400)

        api_key_obj = ApikeySerializer.generate_api_key_for_user(user_obj=user_obj)

        serializer = ApikeySerializer(api_key_obj)
        return Response(serializer.data, status=201)

    def patch(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return Response({"message": "Unauthorized access"}, status=403)

        try:
            user_obj = UserModel.objects.get(pk=self.request.user.pk)
        except UserModel.DoesNotExist:
            return Response({"message": "User Does Not exist"}, status=403)

        try:
            ApikeyModel.objects.get(user=user_obj).delete()
        except ApikeyModel.DoesNotExist:
            return Response({"message": "Apikey does not exists"}, status=404)

        api_key_obj = ApikeySerializer.generate_api_key_for_user(user_obj=user_obj)

        serializer = ApikeySerializer(api_key_obj)
        return Response(serializer.data, status=200)


class LogoutView(APIView):
    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            logout(self.request)
            return Response(status=204)
        return Response(status=401)
