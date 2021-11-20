from matrix import models
from rest_framework import serializers


class LabelSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Label
        fields = '__all__'


class CollectionSerializer(serializers.ModelSerializer):
    labels = serializers.SerializerMethodField('get_labels')

    def get_labels(self, name: str):
        labels = models.Collection.objects.get(name=name).labels.filter(active=True)
        return [label.text for label in labels]

    class Meta:
        model = models.Collection
        exclude = ['active']
