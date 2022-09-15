from django.http import HttpResponse
from django.views.generic import TemplateView


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

class Cerrar_sesionPageView(TemplateView):
    template_name = "cerrar_sesion.html"

    #cachaste lo que pasa¿

