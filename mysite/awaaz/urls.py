from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # when user come to the root/hompage, anything that is in index function of views.py will be executed or rendered
    path('query', views.query, name='query')
]