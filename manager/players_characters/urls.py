from django.urls import path

from . import views

urlpatterns = [
    path("", views.PlayersCharactersListView.as_view(), name="players-characters-list"),
    path(
        "create",
        views.PlayersCharactersCreateView.as_view(),
        name="players-characters-creation",
    ),
    path(
        "update/<int:pk>",
        views.PlayersCharactersUpdateView.as_view(),
        name="players-characters-update",
    ),
]
