from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils.http import url_has_allowed_host_and_scheme

from .access import is_admin_user


def login(request):
    if is_admin_user(request.user):
        return redirect("dashboard:dashboard")

    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")
        user = authenticate(request, username=username, password=password)

        if user is None:
            messages.error(request, "Invalid username or password.")
            return render(request, "authentication/login.html")

        if not is_admin_user(user):
            messages.error(request, "Permission denied. Superuser access is required.")
            return render(request, "authentication/login.html", status=403)

        auth_login(request, user)
        messages.success(request, "Login successful. Welcome to the admin dashboard.")

        next_url = request.GET.get("next")
        if next_url and url_has_allowed_host_and_scheme(next_url, allowed_hosts={request.get_host()}):
            return redirect(next_url)

        return redirect("dashboard:dashboard")

    return render(request, "authentication/login.html")


def register(request):
    return render(request, "authentication/register.html")


def logout(request):
    auth_logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect(reverse("authentication:login"))
