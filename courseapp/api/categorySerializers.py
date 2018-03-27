from rest_framework import serializers
from courseapp.models import Category
from .courseSerializers import CourseSerializerR


class CategorySerializerR(serializers.ModelSerializer):
    """
    Serializer for data retrieval and deletion from `category` model.

    {
        cat_id,
        cat_name,
        cat_desc,
        courses,
        date_created,
        date_modified
    }
    """
    cat_id = serializers.IntegerField(required=False, read_only=True)
    cat_name = serializers.CharField(required=True, max_length=50)
    cat_desc = serializers.CharField(max_length=200)
    courses = CourseSerializerR(many=True)
    date_created = serializers.DateTimeField(read_only=True)
    date_modified = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Category
        fields = [
            'cat_id',
            'cat_name',
            'cat_desc',
            'courses',
            'date_created',
            'date_modified',
        ]


class CategorySerializerCUD(serializers.ModelSerializer):
    """
    Serializer for data creation and updation on `Category` model.

    {
        "cat_name": "",
        "cat_desc": ""
    }
    """
    cat_id = serializers.IntegerField(required=False, read_only=True)
    cat_name = serializers.CharField(required=True, max_length=50)
    cat_desc = serializers.CharField(max_length=200)
    date_created = serializers.DateTimeField(read_only=True)
    date_modified = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Category
        fields = [
            'cat_id',
            'cat_name',
            'cat_desc',
            'date_created',
            'date_modified',
        ]