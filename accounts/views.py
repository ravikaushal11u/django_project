from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .models import AdminUser

User = get_user_model()


def register(request):

    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":

        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm = request.POST.get("confirm-password")

        if password != confirm:
            messages.error(request, "Passwords do not match.")
            return redirect("register")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect("register")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return redirect("register")

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        messages.success(request, "Registration successful.")
        return redirect("login")

    return render(request, "register.html")


def login(request):

    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user:

            auth_login(request, user)

            messages.success(request, "Login Successful.")

            return redirect("home")

        messages.error(request, "Invalid Username or Password.")

    return render(request, "login.html")


@login_required
def logout(request):

    auth_logout(request)

    messages.success(request, "Logout Successful.")

    return redirect("login")

    
  
def admin_logout(request):

    auth_logout(request)

    messages.success(request, "Logout Successful.")

    return redirect("home")

def admnl(request):

    if request.session.get("admin_login"):
        return redirect("messages")   # ya admin dashboard

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            admin = AdminUser.objects.get(username=username)

            if admin.password == password:

                request.session["admin_login"] = True
                request.session["admin_name"] = admin.username

             

            else:
                messages.error(request, "Wrong Password")

        except AdminUser.DoesNotExist:
            messages.error(request, "Admin not found")

    return render(request, "admnl.html")