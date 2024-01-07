from django_filters import FilterSet, DateFilter
from .models import Post
from django import forms


class PostFilter(FilterSet):

    date = DateFilter(field_name='date_in', widget=forms.DateInput(attrs={'type': 'date'}),
                      label='По дате', lookup_expr='date__gte')

    class Meta:
        model = Post

        fields = {
                'title': ['icontains'],
                'date_in': ['lte'],
                'text': ['icontains']
        }
