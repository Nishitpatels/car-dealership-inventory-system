from django.shortcuts import render


def purchase_history(request):
    return render(request, "purchases/purchase_history.html")
