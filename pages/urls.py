from django.urls import path
from .views import (
    HomePageView,
    AboutPageView,
    LoginPageView,
    RegisterPageView,
    CRUDPageView,
)

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("login/", LoginPageView.as_view(), name="login"),
    path("register/", RegisterPageView.as_view(), name="register"),
    path("CRUD/", CRUDPageView.as_view(), name="CRUD"),
]
