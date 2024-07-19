from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView
from .models import *
from .forms import *
from django.db.models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout



class StarsList(ListView):
    model = Stars
    template_name = 'stars/index.html'
    context_object_name = 'stars'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        professions = Profession.objects.annotate(cnt=Count('stars')).filter(cnt__gt=0)
        context['professions'] = professions
        context['title'] = 'Звезды'
        return context

    def get_queryset(self):
        return Stars.objects.all().select_related('profession')


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
        return Stars.objects.filter(profession__id=self.kwargs['profession_id']).select_related('profession')


class AddStar(LoginRequiredMixin, CreateView):
    form_class = StarForm
    template_name = 'stars/add_form.html'
    login_url = '/admin/'

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


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'stars/register.html', {'form': form})


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main')
    else:
        form = AuthenticationForm()

    return render(request, 'stars/login.html', {'form': form}) 

 
def user_logout(request):
    logout(request)
    return redirect('main')