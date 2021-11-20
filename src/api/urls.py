from . import views
from django.urls import path

app_name = 'api'
urlpatterns = [
    path('collection/<str:name>/', views.CollectionAV.as_view(), name='collection')
]
