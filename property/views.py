from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Property

# Create your views here.
class PropertyListView(ListView):
    model = Property
    ### filter
    ### pagination

class PropertyDetailView(DetailView):
    model = Property
    
    ### book