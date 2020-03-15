from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.list_employe, name="list_employe"),
    path('add/', views.add_employe, name="add_employe"),
    path('details/<int:id>', views.details_employe, name="details_employe"),
    path('remove/<int:id>', views.remove_employe, name="remove_employe"),
]
