"""
Refer to doc.org file for documentation of this code.
"""

from rest_framework import generics
from courseapp.models import Litem
from .litemSerializers import LitemSerializer

class LitemCreate(generics.CreateAPIView):
    serializer_class = LitemSerializer
    queryset = Litem.objects.all()

class LitemList(generics.ListAPIView):
    serializer_class = LitemSerializer
    queryset = Litem.objects.all()