from .models import Post
import django_filters

class PostFilter(django_filters.FilterSet):

    CHOICES = (
        ('ascending', 'Legrégebbi elől'),
        ('descending', 'Legújabb elől')
    )

    ordering = django_filters.ChoiceFilter(label='Rendezés', choices=CHOICES, method="filter_by_order")

    class Meta:
        model = Post
        fields = {
            'cim': ['icontains'],
        }

    def filter_by_order(self, queryset, name, value):
        expression = 'kelt' if value == 'ascending' else '-kelt'
        return queryset.order_by(expression)
