from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from account.authentication import ApiKeyAuthentication

class SecureAPIView(APIView):
    authentication_classes = [ApiKeyAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"msg": f"Hello {request.user.email}!"})
