import django_filters
from .models import Book, Tag


# class BookFilter(django_filters.FilterSet):
#     class Meta:
#         model = Book
#         fields ={
#             'title': ['icontains'],
#             'tags': ['exact'],
#         }

class BookFilter(django_filters.FilterSet):
    tags = django_filters.ModelChoiceFilter(queryset=Tag.objects.all().order_by('name'), label="Kategorie:")
    o = django_filters.OrderingFilter(
        fields=('title','author'), label='Sortowanie:', field_labels={'title': 'Tytuł', 'author': 'Autor',
                                                                      '-title': 'Tytuł (malejąco)', '-author': 'Autor (malejąco)'}
    )
    class Meta:
        model = Book
        fields = ['tags']







