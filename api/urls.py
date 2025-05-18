from django.urls import path
from api.views import SecureAPIView

urlpatterns = [
    path("", SecureAPIView.as_view(), name="secure_view")
]
