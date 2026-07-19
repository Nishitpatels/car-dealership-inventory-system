from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import ContactMessageForm


def home(request):
    return render(request, "core/home.html")


def about(request):
    return render(request, "core/about.html")


def contact(request):
    if request.method == "POST":
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully.")
            return redirect("core:contact")

        for field, errors in form.errors.items():
            label = form.fields[field].label if field in form.fields else "Contact"
            for error in errors:
                messages.error(request, f"{label}: {error}")

    return render(request, "core/contact.html")


def not_found(request):
    return render(request, "core/404.html")


def page_not_found(request, exception):
    return render(request, "core/404.html", status=404)


def permission_denied(request, exception):
    return render(request, "core/403.html", status=403)


def server_error(request):
    return render(request, "core/500.html", status=500)
