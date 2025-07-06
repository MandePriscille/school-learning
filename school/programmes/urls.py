from django.urls import path
from programmes.views import NiveauListView, MatiereListView

app_name = "programmes"
urlpatterns = [
    path('listes-niveau/', NiveauListView.as_view(), name="list_niveau"),
    path('list matier/<slug:slug>/', MatiereListView.as_view(), name="list_matiere")
]
