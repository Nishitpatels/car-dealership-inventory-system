from django.shortcuts import render

from authentication.access import admin_required


@admin_required
def dashboard(request):
    return render(request, "dashboard/dashboard.html")


@admin_required
def user_management(request):
    return render(request, "dashboard/user_management.html")


@admin_required
def profile(request):
    return render(request, "dashboard/profile.html")


@admin_required
def settings(request):
    return render(request, "dashboard/settings.html")
