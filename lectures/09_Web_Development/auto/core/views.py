# Create your views here.
from django.shortcuts import render_to_response
from core.models import Auto
from django.db.models import Sum


def leaderboard_index(request):

    auto_items = Auto.objects.annotate(
        value=Sum("sale__price")
    ).order_by('-value')

    context = {
        "auto_items": auto_items
    }

    return render_to_response("index.html", context=context)
