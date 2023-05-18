from django.forms import DateTimeInput, DateInput
from django_filters import FilterSet, ModelChoiceFilter, DateTimeFilter
from .models import Post, Category


class PostFilter(FilterSet):

    category = ModelChoiceFilter(
        field_name="postcategory__category",
        queryset=Category.objects.all(),
        label='Category',
        empty_label='all',
    )

    time_creation = DateTimeFilter(
        field_name='time_creation',
        lookup_expr='gt',
        widget=DateTimeInput(
        # widget=DateInput(
            format='%Y-%m-%dT%H:%M',
            # format='%Y-%m-%d',
            attrs={'type': 'datetime-local'},
        ),
    )

    class Meta:
        # В Meta классе мы должны указать Django модель,
        # в которой будем фильтровать записи.
        model = Post
        # В fields мы описываем по каким полям модели
        # будет производиться фильтрация.
        fields = {
            # поиск по названию
            'title': ['icontains'],
            # количество товаров должно быть больше или равно
            # 'time_creation': ['gt'],
        }
