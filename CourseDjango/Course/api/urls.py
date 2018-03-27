from django.urls import path
from .views import BulkCategoryView

urlpatterns = [
    path('bulk/category', BulkCategoryView.as_view(), name='bulk-category')
]
