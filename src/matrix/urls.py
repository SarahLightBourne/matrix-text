from . import views
from django.urls import path

app_name = 'homepage'
urlpatterns = [
    path('', views.index_view, name='index'),
    path('<str:name>/', views.CollectionView.as_view(), name='collection')
]
