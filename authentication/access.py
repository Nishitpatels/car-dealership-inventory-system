from functools import wraps
from urllib.parse import quote

from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse


def is_admin_user(user):
    return user.is_authenticated and user.is_staff and user.is_superuser


def admin_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.warning(request, "Please log in with your administrator account.")
            login_url = reverse("authentication:login")
            return redirect(f"{login_url}?next={quote(request.get_full_path())}")

        if not is_admin_user(request.user):
            messages.error(request, "Permission denied. Superuser access is required.")
            return render(request, "core/404.html", status=403)

        return view_func(request, *args, **kwargs)

    return wrapper
