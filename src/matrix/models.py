from django.db import models


class Collection(models.Model):
    name = models.CharField('Name', max_length=25, unique=True)
    active = models.BooleanField('Active', default=True)

    def __str__(self) -> str:
        return self.name


class Label(models.Model):
    collection = models.ForeignKey(
        Collection,
        on_delete=models.CASCADE,
        verbose_name='Collection',
        related_name='labels'
    )

    text = models.CharField('Text', max_length=50)
    active = models.BooleanField('Active', default=True)

    def __str__(self) -> str:
        return self.text
