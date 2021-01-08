from django.views.generic import ListView
from . import models

# class based views
class HomeView(ListView):

    """ Hemo View Definition """

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"