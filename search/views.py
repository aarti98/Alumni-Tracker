from django.shortcuts import render
from django.views.generic import ListView
from authentication.models import CustomUser


class SearchResultView(ListView):
    model = CustomUser
    template_name = 'search/results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = CustomUser.objects.filter(username=query)
        return object_list