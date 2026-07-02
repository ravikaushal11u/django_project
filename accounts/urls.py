from django.urls import path
from . import views

urlpatterns = [

    path("", views.login, name="login"),

    path("register/", views.register, name="register"),

    path("logout/", views.logout, name="logout"),
   path("admnl/", views.admnl, name="admnl"),
     path("admin/logout/", views.admin_logout, name="admin_logout"), 

]