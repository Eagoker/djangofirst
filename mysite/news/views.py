from .models import *
from .forms import *
from django.views.generic import ListView, DetailView, CreateView


class NewsList(ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'news'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Main'
        categories = Category.objects.all()
        context['categories'] = categories
        return context
    
    def get_queryset(self):
        return News.objects.filter(is_published=True)


class NewsCategory(ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'news'
    
    def get_queryset(self):
        return News.objects.filter(category__id=self.kwargs['category_id'], is_published=True)


class ViewNews(DetailView):
    model = News
    template_name = 'news/view_news.html'
    pk_url_kwarg = 'news_id'
    context_object_name = 'news_item'


class AddNew(CreateView):
    form_class = NewForm
    template_name = 'news/add_new.html'
    
