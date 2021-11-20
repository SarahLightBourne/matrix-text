from django.views import generic
from django.shortcuts import redirect


def index_view(request):
    return redirect('matrix:collection', name='hello')


class CollectionView(generic.TemplateView):
    template_name = 'matrix/collection.html'
