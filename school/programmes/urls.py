from django.urls import path
from programmes.views import NiveauListView, MatiereListView, LessonListView

app_name = "programmes"
urlpatterns = [
    path('listes-niveau/', NiveauListView.as_view(), name="list_niveau"),
    path('list matier/<slug:slug>/', MatiereListView.as_view(), name="list_matiere"),
    path('list lesson/<str:niveau>/<slug:slug>/', LessonListView.as_view(), name="list_lesson")
]
