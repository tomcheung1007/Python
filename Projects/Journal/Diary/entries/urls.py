from django.urls import path
from . import views


# paths must have at least two arguments
# 1. a route string pattern which contains a URL pattern
# 2. refernce to a view which is an as_view() function
urlpatterns = [
    path("", views.EntryListView.as_view(), name="entry-list"),
    path(
        "entry/<int:pk>", views.EntryDetailView.as_view(), name="entry-detail"
    ),
    path("create", views.EntryCreateView.as_view(), name="entry-create"),
    path(
        "entry/<int:pk>/update",
        views.EntryUpdateView.as_view(),
        name="entry-update",
    ),
    path(
        "entry/<int:pk>/delete",
        views.EntryDeleteView.as_view(),
        name="entry-delete",
    ),
]

