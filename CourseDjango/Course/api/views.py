from rest_framework.generics import (
    ListAPIView,
)
from .serializers import BulkCategorySerializer
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import PermissionDenied
from ..models import Category


class BulkCategoryView(ListAPIView):
    """
    Lists All the Category with each course, lessons & lession items respectively.
    """
    serializer_class = BulkCategorySerializer
    permission_classes = [AllowAny]
    authentication_classes = []

    def get_queryset(self):
        """
        Returns a queryset of all Categories
        """
        try:
            return Category.objects.all()
        except Exception as e:
            raise PermissionDenied
