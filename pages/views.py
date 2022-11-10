from django.http import HttpResponse
from django.views.generic import TemplateView
from users.models import Habito


def homePageView(request):
    return HttpResponse("Hola mundo!")


class HomePageView(TemplateView):
    template_name = "home.html"


class AboutPageView(TemplateView):
    template_name = "about.html"


class LoginPageView(TemplateView):
    template_name = "login.html"


class RegisterPageView(TemplateView):
    template_name = "register.html"


class CRUDPageView(TemplateView):
    template_name = "CRUD.html"
