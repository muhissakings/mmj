from xmlrpc.server import list_public_methods
from django.urls import path
from .import views


urlpatterns = [
    path("create", views.createTrainees, name="create"),
    path("listtrainees", views.listAllTrainees, name="listTrainees"),
    path("edittrainees/<int:id>", views.editTrainees, name="edittrainees"),
    path("updatetrainees/<int:id>", views.updateTrainees, name="updatetrainees"),
    path("delete/<int:id>", views.deleteTrainees, name="delete"),
    path("login", views.login, name="login")
]
