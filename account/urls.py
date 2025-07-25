from django.urls import path

from account.views import ApikeyView, LoginView, LogoutView, RegisterView

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("register/", RegisterView.as_view(), name="register"),
    path("api-key/", ApikeyView.as_view(), name="api_key"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
