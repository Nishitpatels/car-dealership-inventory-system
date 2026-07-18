from django.shortcuts import render


def dashboard(request):
    return render(request, "dashboard/dashboard.html")


def user_management(request):
    return render(request, "dashboard/user_management.html")


def profile(request):
    return render(request, "dashboard/profile.html")


def settings(request):
    return render(request, "dashboard/settings.html")
