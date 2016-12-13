from django.shortcuts import render_to_response
from core.models import Artist
from django.db.models import Sum


def leaderboard_index(request):

    artists = Artist.objects.annotate(
        capital=Sum("ruble__nominal")
    ).order_by('-capital')

    context = {
        "artists": artists
    }

    return render_to_response("index.html", context=context)
