from django.urls import path

from . import views

app_name = "characters"
urlpatterns = [
    path("", views.PlayersCharactersListView.as_view(), name="players-characters-list"),
    path(
        "<int:pk>",
        views.PlayersCharactersDetails.as_view(),
        name="players-characters-details",
    ),
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
    path(
        "delete/<int:pk>",
        views.PlayersCharactersDeleteView.as_view(),
        name="delete-characters",
    ),
]
