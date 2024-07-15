from django.urls import path
from .views import *

urlpatterns = [
    # path('', index, name="home"),
    path('', NewsList.as_view(), name="home"),
    path('category/<int:category_id>/', NewsCategory.as_view(), name="category"),
    path('news/<int:news_id>/', ViewNews.as_view(), name="view_news"),
    path('news/add-new/', AddNew.as_view(), name="add_new"),
]
