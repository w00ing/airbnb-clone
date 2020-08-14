from django.shortcuts import render, redirect
from django.http import Http404
from django.urls import reverse
from django.views.generic import ListView, DetailView
from . import models


class HomeView(ListView):

    """ HomeView Definition """

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "rooms"


class RoomDetail(DetailView):

    """ Room Detail Definition """

    model = models.Room
    # context_object_name = "room"

