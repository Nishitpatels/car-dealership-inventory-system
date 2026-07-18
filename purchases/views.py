from django.shortcuts import render

from authentication.access import admin_required


@admin_required
def purchase_history(request):
    return render(request, "purchases/purchase_history.html")
