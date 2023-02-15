from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import views

app_name = "accounts"

urlpatterns = [
    path(
        "entrar/",
        LoginView.as_view(
            template_name="accounts/login.html", redirect_authenticated_user=True
        ),
        name="login",
    ),
    path("sair/", LogoutView.as_view(), name="logout"),
    path("criar_conta/", views.signup, name="signup"),
]
