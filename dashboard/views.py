from django.contrib import messages
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from authentication.access import admin_required
from authentication.forms import AdminInviteUserForm, AdminProfileForm
from core.models import ContactMessage


def _add_form_errors_to_messages(request, form, default_label="Form"):
    for field, errors in form.errors.items():
        label = form.fields[field].label if field in form.fields else default_label
        for error in errors:
            messages.error(request, f"{label}: {error}")


@admin_required
def dashboard(request):
    return render(request, "dashboard/dashboard.html")


@admin_required
def user_management(request):
    return render(request, "dashboard/user_management.html")


@admin_required
def invite_user(request):
    if request.method == "POST":
        form = AdminInviteUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f"User created successfully. {user.username} can now sign in.")
            return redirect("dashboard:user_management")
        _add_form_errors_to_messages(request, form, "Invite user")

    return render(request, "dashboard/invite_user.html")


@admin_required
def profile(request):
    if request.method == "POST":
        form = AdminProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Admin profile updated successfully.")
            return redirect("dashboard:profile")
        _add_form_errors_to_messages(request, form, "Profile")

    return render(request, "dashboard/profile.html")


@admin_required
def settings(request):
    return render(request, "dashboard/settings.html")


@require_POST
@admin_required
def deactivate_user(request):
    user_id = request.POST.get("user_id")
    user = get_user_model().objects.filter(pk=user_id).first()

    if user is None:
        messages.error(request, "User not found.")
    elif user.is_superuser:
        messages.error(request, "Superuser accounts cannot be deactivated from User Management.")
    else:
        user.is_active = False
        user.save(update_fields=["is_active"])
        messages.success(request, f"{user.username} has been deactivated.")

    return redirect("dashboard:user_management")


@admin_required
def contact_messages(request):
    return render(request, "dashboard/contact_messages.html")


@require_POST
@admin_required
def delete_contact_message(request):
    message = get_object_or_404(ContactMessage, pk=request.POST.get("message_id"))
    message.delete()
    messages.success(request, "Contact message deleted successfully.")
    return redirect("dashboard:contact_messages")
