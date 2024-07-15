from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from .models import *
from .forms import *


class StarsList(ListView):
    model = Stars
    template_name = 'stars/index.html'
    context_object_name = 'stars'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        professions = Profession.objects.all()
        context['professions'] = professions
        context['title'] = 'Звезды'
        return context

    def get_queryset(self):
        return Stars.objects.all()


class ByProfession(ListView):
    model = Stars
    template_name = 'stars/index.html'
    context_object_name = 'stars'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        professions = Profession.objects.all()
        context['professions'] = professions
        context['title'] = 'Звезды'
        return context

    def get_queryset(self):
        return Stars.objects.filter(profession__id=self.kwargs['profession_id'])


class AddStar(CreateView):
    form_class = StarForm
    template_name = 'stars/add_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        professions = Profession.objects.all()
        context['professions'] = professions
        context['title'] = 'Звезды'
        return context


class ViewStar(DetailView):
    model = Stars
    template_name = 'stars/star.html'
    pk_url_kwarg = 'star_id'
    context_object_name = 'star'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        professions = Profession.objects.all()
        context['professions'] = professions
        context['title'] = 'Звезды'
        return context
