from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

from account.models import ApikeyModel


class ApiKeyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        api_key = request.headers.get("X-API-KEY")

        if not api_key:
            raise AuthenticationFailed("API key missing")

        try:
            api_key_obj = ApikeyModel.objects.get(api_key=api_key)

        except ApikeyModel.DoesNotExist:
            raise AuthenticationFailed("Invalid API key")

        return (api_key_obj.user, None)
