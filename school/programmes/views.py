from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Niveaux, Lesson, Matiere


class NiveauListView(ListView):
    model = Niveaux
    template_name = 'programmes/nivaulist.html'
    context_object_name = 'niveaux'


class MatiereListView(DetailView):
    model = Niveaux
    template_name = 'programmes/matierelist.html'
    context_object_name = 'niveaux'


