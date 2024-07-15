from django.urls import path, include
from .views import *

urlpatterns = [
    path('', StarsList.as_view(), name='main'),
    path('profession/<int:profession_id>/', ByProfession.as_view(), name='by_profession'),
    path('add-star/', AddStar.as_view(), name='add_star'),
    path('view-star/<int:star_id>/', ViewStar.as_view(), name='view_star'),

]