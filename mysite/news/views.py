from django.shortcuts import render, redirect
from .models import News, Category
from .forms import NewForm


def index(request):
    news = News.objects.all()
    categories = Category.objects.all()
    context = {
        'news': news,
        'title': 'News list',
        'categories': categories,
    }
    return render(request, 'news/index.html', context)


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    categories = Category.objects.all()
    context = {
        'news': news,
        'category': category,
        'categories': categories,
    }
    return render(request, template_name='news/category.html', context=context)


def view_news(request, news_id):
    news_item = News.objects.get(pk=news_id)
    context = {
        'news_item': news_item
    }
    return render(request, template_name='news/view_news.html', context=context)


def add_new(request):
    if request.method == 'POST':
        form = NewForm(request.POST)
        if form.is_valid():
            new = form.save()
            return redirect(new)
    else:
        form = NewForm()
    return render(request, 'news/add_new.html', context={'form': form})
