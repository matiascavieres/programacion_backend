from django.urls import path
from .views import HomePageView, AboutPageView , LoginPageView, Sign_UpPageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("login/", LoginPageView.as_view(), name="login"),
    path("sign_up/", Sign_UpPageView.as_view(), name="sign_up"),
]
