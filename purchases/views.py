from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist, PermissionDenied, ValidationError
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils.http import url_has_allowed_host_and_scheme
from django.views.decorators.http import require_POST

from authentication.access import login_required_frontend

from .forms import PurchaseForm
from .services import purchase_vehicle


def _safe_redirect_target(request, fallback_name):
    referer = request.META.get("HTTP_REFERER")
    if referer and url_has_allowed_host_and_scheme(referer, allowed_hosts={request.get_host()}):
        return referer
    return reverse(fallback_name)


@login_required_frontend
def purchase_history(request):
    return render(request, "purchases/purchase_history.html")


@require_POST
@login_required_frontend
def purchase_vehicle_view(request):
    form = PurchaseForm(request.POST)
    redirect_url = _safe_redirect_target(request, "inventory:inventory")

    if not form.is_valid():
        for errors in form.errors.values():
            for error in errors:
                messages.error(request, error)
        return redirect(redirect_url)

    try:
        purchase = purchase_vehicle(
            user=request.user,
            vehicle_id=form.cleaned_data["vehicle_id"],
            quantity=form.cleaned_data["quantity"],
        )
    except ObjectDoesNotExist:
        messages.error(request, "Vehicle not found.")
    except PermissionDenied as error:
        messages.error(request, str(error))
    except ValidationError as error:
        messages.error(request, error.messages[0] if hasattr(error, "messages") else str(error))
    else:
        messages.success(request, f"Purchase completed for {purchase.vehicle}.")

    return redirect(redirect_url)
