from . import serializers
from matrix import models

from rest_framework import generics


class CollectionAV(generics.RetrieveAPIView):
    queryset = models.Collection.objects.filter(active=True)
    serializer_class = serializers.CollectionSerializer
    lookup_field = 'name'
