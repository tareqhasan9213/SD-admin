from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.index, name = 'index'),
    path('card',views.card, name = 'card'),
    path('chart', views.chart, name='chart'),
    path('table',views.table, name='table')
]
