from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils.http import url_has_allowed_host_and_scheme

from .access import is_admin_user, login_required_frontend
from .forms import AdminLoginForm, UserLoginForm, UserRegistrationForm


def _apply_remember_me(request):
    if not request.POST.get("remember_me"):
        request.session.set_expiry(0)


def login(request):
    if is_admin_user(request.user):
        return redirect("dashboard:dashboard")
    if request.user.is_authenticated:
        return redirect("authentication:profile")

    if request.method == "POST":
        form = UserLoginForm(request.POST, request=request)

        if form.is_valid():
            auth_login(request, form.get_user())
            _apply_remember_me(request)
            messages.success(request, "Login successful.")

            next_url = request.GET.get("next")
            if next_url and url_has_allowed_host_and_scheme(next_url, allowed_hosts={request.get_host()}):
                return redirect(next_url)

            return redirect("core:home")

        for error in form.non_field_errors():
            messages.error(request, error)

    return render(request, "authentication/login.html")


def admin_login(request):
    if is_admin_user(request.user):
        return redirect("dashboard:dashboard")

    if request.method == "POST":
        form = AdminLoginForm(request.POST, request=request)

        if form.is_valid():
            auth_login(request, form.get_user())
            _apply_remember_me(request)
            messages.success(request, "Login successful. Welcome to the admin dashboard.")

            next_url = request.GET.get("next")
            if next_url and url_has_allowed_host_and_scheme(next_url, allowed_hosts={request.get_host()}):
                return redirect(next_url)

            return redirect("dashboard:dashboard")

        for error in form.non_field_errors():
            messages.error(request, error)

    return render(request, "authentication/admin_login.html")


def register(request):
    if request.user.is_authenticated:
        if is_admin_user(request.user):
            return redirect("dashboard:dashboard")
        return redirect("authentication:profile")

    if request.method == "POST":
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful. Please log in.")
            return redirect("authentication:login")

        for field, errors in form.errors.items():
            label = form.fields[field].label if field in form.fields else "Registration"
            for error in errors:
                messages.error(request, f"{label}: {error}")

    return render(request, "authentication/register.html")


def logout(request):
    redirect_name = "authentication:admin_login" if is_admin_user(request.user) else "authentication:login"
    auth_logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect(reverse(redirect_name))


@login_required_frontend
def profile(request):
    return render(request, "authentication/profile.html")


@login_required_frontend
def user_dashboard(request):
    if is_admin_user(request.user):
        return redirect("dashboard:dashboard")
    return render(request, "authentication/user_dashboard.html")
