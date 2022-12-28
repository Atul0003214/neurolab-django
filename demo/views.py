from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView,CreateView,UpdateView
from django.contrib.auth.views import LoginView,LogoutView
# Create your views here.

from . models import Cart

class LogInInterfaceView(LoginView):
    template_name = "demo/login.html"

class LogOutInterfaceView(LogoutView):
    template_name = "demo/logout.html"

class IndexView(TemplateView):
    template_name = "demo/index.html"

# def index(request):
#     return HttpResponse("woking!!!!")


class ProductView(TemplateView):
    template_name = "demo/index.html"

class AuthrizedView(LoginRequiredMixin,ListView):
    model = Cart
    login_url = '/demo/login'
    template_name = 'demo/cart.html'
    # success_url = "product"


# def cart(LoginRequiredMixin,request):
#     login_url = 'admin/'

def order(LoginRequiredMixin,request):
    return HttpResponse("order!!!!")




