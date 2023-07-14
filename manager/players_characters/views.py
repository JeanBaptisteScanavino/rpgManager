from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from players_characters.models import PlayersCharacters


class PlayersCharactersListView(ListView):
    model = PlayersCharacters
    paginate_by = 100
    template_name = "players_characters/list.html"


class PlayersCharactersCreateView(CreateView):
    model = PlayersCharacters
    fields = ["name", "player", "character_sheet_url"]
    template_name = "players_characters/creation.html"
    success_url = reverse_lazy("players-characters-list")


class PlayersCharactersUpdateView(UpdateView):
    model = PlayersCharacters
    fields = ["name", "player", "character_sheet_url"]
    template_name = "players_characters/update.html"
    success_url = reverse_lazy("players-characters-list")
