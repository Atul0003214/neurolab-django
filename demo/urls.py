from django.urls import path
from . import views

urlpatterns = [
    path("",views.IndexView.as_view()),
    path("product", views.ProductView.as_view()),
    path("cart",views.AuthrizedView.as_view()),
    path("order",views.order),
    path("login",views.LogInInterfaceView.as_view()),
    path("logout",views.LogOutInterfaceView.as_view()),
]

