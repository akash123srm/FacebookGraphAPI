from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView

# Create your views here.


class LoginView(TemplateView):
    template_name = "login.html"

    '''@method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginView, self).dispatch(*args, **kwargs)'''

    def get_context_data(self, **kwargs):
        pass




class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
       pass
