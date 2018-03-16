from rest_framework import generics
from courseapp.models import Litem
from .litemSerializers import LitemSerializerCUD, LitemSerializerR


class LitemCreate(generics.CreateAPIView):
    """
    View to create a new `litem`.

    Uses `LitemSerializerCUD` serializer class.
    """
    serializer_class = LitemSerializerCUD
    queryset = Litem.objects.all()


class LitemList(generics.ListAPIView):
    """
    View to list all the `litem` present in `Litem` model.

    Uses `LitemSerializerR` serializer class.
    """
    serializer_class = LitemSerializerR
    queryset = Litem.objects.all()


class LitemRUDView(generics.RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update, delete a `litem`.

    Uses `LitemSerializerR` serializer class to retrieve and
    `LitemSerializerCUD` serializer class to update and delete
    a `litem`.
    """
    queryset = Litem.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return LitemSerializerR
        elif self.request.method == "PUT" or "PATCH" or "DELETE":
            return LitemSerializerCUD
