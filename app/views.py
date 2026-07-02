from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Contact


def home(request):
    return render(request, "home.html")


@login_required(login_url='login')
def about(request):
    return render(request, "about.html")


@login_required(login_url='login')
def projects(request):
    return render(request, "projects.html")


@login_required(login_url='login')
def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        mobile = request.POST.get("mobile")
        budget = request.POST.get("budget")
        message = request.POST.get("message")

        Contact.objects.create(
            name=name,
            email=email,
            mobile=mobile,
            budget=budget,
            message=message
        )

        messages.success(request, "Message sent successfully!")
        return redirect("contact")

    return render(request, "contact.html")


@login_required(login_url='admnl')   # Ya hata do agar session check hi use karna hai
def messages_page(request):
    # Sirf admin session wale hi dekh sakte hain
    if not request.session.get("admin_login"):
        return redirect("admnl")

    contacts = Contact.objects.all().order_by("-id")

    return render(request, "messages.html", {
        "contacts": contacts
    })