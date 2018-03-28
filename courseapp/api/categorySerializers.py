from rest_framework import serializers
from courseapp.models import Category
from .courseSerializers import CourseSerializerR


class CategorySerializerR(serializers.ModelSerializer):
    """
    Serializer for data retrieval from `category` model.

    {
        cat_id,
        cat_name,
        cat_desc,
        cat_icon_url,
        date_created,
        date_modified,
        courses (courses related the category)
    }
    """
    cat_id = serializers.IntegerField(required=False, read_only=True)
    cat_name = serializers.CharField(required=True, max_length=50)
    cat_desc = serializers.CharField(max_length=200)
    cat_icon_url = serializers.URLField(max_length=200, required=False, allow_null=True)
    date_created = serializers.DateTimeField(read_only=True)
    date_modified = serializers.DateTimeField(read_only=True)
    courses = CourseSerializerR(many=True, read_only=True)

    class Meta:
        model = Category
        fields = [
            'cat_id',
            'cat_name',
            'cat_desc',
            'cat_icon_url',
            'date_created',
            'date_modified',
            'courses',
        ]


class CategorySerializerCUD(serializers.ModelSerializer):
    """
    Serializer for data creation and updation on `Category` model.

    {
        cat_name,
        cat_desc,
        cat_icon_url
    }
    """
    cat_id = serializers.IntegerField(required=False, read_only=True)
    cat_name = serializers.CharField(required=True, max_length=50)
    cat_desc = serializers.CharField(max_length=200)
    cat_icon_url = serializers.URLField(max_length=200, required=False, allow_null=True)
    date_created = serializers.DateTimeField(read_only=True)
    date_modified = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Category
        fields = [
            'cat_id',
            'cat_name',
            'cat_desc',
            'cat_icon_url',
            'date_created',
            'date_modified',
        ]