from . import views
from django.urls import path

app_name = 'matrix'
urlpatterns = [
    path('', views.index_view, name='index'),
    path('<str:name>/', views.CollectionView.as_view(), name='collection')
]
