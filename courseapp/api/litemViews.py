"""
Refer to doc.org file for documentation of this code.
"""

from rest_framework import generics
from courseapp.models import Litem
from .litemSerializers import LitemSerializerCUD, LitemSerializerR


class LitemCreate(generics.CreateAPIView):
    serializer_class = LitemSerializerCUD
    queryset = Litem.objects.all()


class LitemList(generics.ListAPIView):
    serializer_class = LitemSerializerR
    queryset = Litem.objects.all()


class LitemRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Litem.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            import pdb
            pdb.set_trace()

            return LitemSerializerR
        elif self.request.method == "PUT" or "PATCH" or "DELETE":
            return LitemSerializerCUD
