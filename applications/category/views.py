
from rest_framework import generics

from applications.category.models import Category
from applications.category.serializers import CategorySerializer


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer