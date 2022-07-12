from msilib.schema import ListView
from django.shortcuts import render

# Create your views here.
class HomePageView(ListView):
    template = "base.html"
