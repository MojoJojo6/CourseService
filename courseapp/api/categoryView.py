from rest_framework import generics
from courseapp.models import Category
from .categorySerializers import CategorySerializerCUD, CategorySerializerR


class CategoryRUDView(generics.RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update or delete a `category`.

    Uses `CategorySerializerR` serializer class for `category` retrieval,
    `CategorySerializerCUD` serializer class to create, update and delete
    a `category`.
    """
    queryset = Category.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return CategorySerializerR
        elif self.request.method == "PUT" or "PATCH" or "DELETE":
            return CategorySerializerCUD


class CategoryList(generics.ListAPIView):
    """
    View to get list of all the `category` present in `Category` model.

    Uses `CategorySerializerR` serializer class.
    """
    serializer_class = CategorySerializerR
    queryset = Category.objects.all()


class CategoryCreate(generics.CreateAPIView):
    """
    View to create a new `category`.

    Uses `CategorySerializerCUD` serializer class.
    """
    serializer_class = CategorySerializerCUD
    queryset = Category.objects.all()