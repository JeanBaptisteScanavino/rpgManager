from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView

from world.models import Regions


class RegionsListView(ListView):
    model = Regions
    paginate_by = 20
    template_name = "regions/list.html"


class RegionsCreateView(CreateView):
    model = Regions
    fields = [
        "name",
        "visited",
        "religion",
        "politic",
        "chief",
        "region_maps_url",
        "description",
        "history_in_campaign",
    ]
    template_name = "regions/creation.html"
    success_url = reverse_lazy("regions-list")


class RegionsUpdateView(UpdateView):
    model = Regions
    fields = [
        "name",
        "visited",
        "religion",
        "politic",
        "chief",
        "region_maps_url",
        "description",
        "history_in_campaign",
    ]
    template_name = "regions/update.html"
    success_url = reverse_lazy("regions-list")
