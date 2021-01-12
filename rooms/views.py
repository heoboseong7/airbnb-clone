from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django_countries import countries
from . import models

# class based views
class HomeView(ListView):

    """ Hemo View Definition """

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "rooms"


def room_detail(request, pk):
    try:
        room = models.Room.objects.get(pk=pk)
        return render(request, "rooms/detail.html", {"room": room})
    except models.Room.DoesNotExist:
        raise Http404()
        # error는 raise로
        # 404에 대한 페이지를 만드려면 template에 해당하는 404.html을 생성


class RoomDetail(DetailView):

    """ RoomDetail Definition """

    model = models.Room


def search(request):
    city = request.GET.get("city", "Anywhere")
    city = str.capitalize(city)
    country = request.GET.get("country", "KR")
    room_type = int(request.GET.get("room_type", 0))
    room_types = models.RoomType.objects.all()

    form = {
        "city": city,
        "s_room_type": room_type,
        "s_country": country,
    }

    choices = {
        "countries": countries,
        "room_types": room_types,
    }
    return render(
        request,
        "rooms/search.html",
        {**form, **choices},
    )
