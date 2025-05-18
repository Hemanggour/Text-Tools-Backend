import secrets

from rest_framework import serializers

from account.models import ApikeyModel, UserModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ["email", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = UserModel(email=validated_data.get("email"))
        user.set_password(validated_data.get("password"))
        user.save()
        return user


class ApikeySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApikeyModel
        fields = ["api_key", "created_at"]
        extra_kwargs = {
            "api_key": {"read_only": True},
            "created_at": {"read_only": True},
        }

    @staticmethod
    def generate_api_key_for_user(user_obj):
        api_key = secrets.token_urlsafe(50)
        apikey_obj = ApikeyModel.objects.create(user=user_obj, api_key=api_key)
        apikey_obj.save()
        return apikey_obj
