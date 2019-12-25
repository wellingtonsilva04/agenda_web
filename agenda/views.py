from django.shortcuts import render
from django.template import loader
from django.views import generic

from .models import Contato
# Create your views here.
class IndexView(generic.ListView):
    template_name = 'agenda/index.html'
    context_object_name = 'contatos_list'
    def get_queryset(self):
        """Return the five contatos."""
        return Contato.objects.all()[:5]


class DetailView(generic.DetailView):
    model = Contato
    template_name = 'agenda/detailContato.html'
