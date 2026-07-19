from django.shortcuts import render


def home(request):
    return render(request, "core/home.html")


def about(request):
    return render(request, "core/about.html")


def contact(request):
    return render(request, "core/contact.html")


def not_found(request):
    return render(request, "core/404.html")


def page_not_found(request, exception):
    return render(request, "core/404.html", status=404)


def permission_denied(request, exception):
    return render(request, "core/403.html", status=403)


def server_error(request):
    return render(request, "core/500.html", status=500)
