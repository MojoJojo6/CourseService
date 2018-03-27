from ..models import (
    Category,
    Course,
    Lesson,
    Lessons_item
)
from rest_framework import serializers


class Lesson_itemSerializer(serializers.ModelSerializer):
    """
    Serializer for Lesson Item Model
    """
    id                      = serializers.IntegerField(required=False, read_only=True)
    lesson_item_name        = serializers.CharField(max_length=20)
    lesson_item_seqname     = serializers.IntegerField()
    lesson_item_description = serializers.CharField(max_length=200)
    lesson_item_asset_link =  serializers.CharField(max_length=200)
    date_created            = serializers.DateTimeField(read_only=True)
    date_modified           = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Lessons_item
        fields = [
            'id',
            'lesson_item_name',
            'lesson_item_seqname',
            'lesson_item_description',
            'lesson_item_asset_link',
            'date_created',
            'date_modified'
        ]


class BulkLessonSerializer(serializers.ModelSerializer):
    """
    Serializer for Lesson Model
    """
    id                  = serializers.IntegerField(required=False, read_only=True)
    lesson_name         = serializers.CharField(max_length=20)
    lesson_seqname      = serializers.IntegerField()
    lesson_description  = serializers.CharField(max_length=200)
    date_created        = serializers.DateTimeField(read_only=True)
    date_modified       = serializers.DateTimeField(read_only=True)
    lesson_items       = Lesson_itemSerializer(many=True, read_only=True)

    class Meta:
        model = Lesson
        fields = [
            'id',
            'lesson_name',
            'lesson_seqname',
            'lesson_description',
            'date_created',
            'date_modified',
            'lesson_items'
        ]


class BulkCourseSerializer(serializers.ModelSerializer):
    """
    Serializer for Course Model
    """
    id                  = serializers.IntegerField(required=False, read_only=True)
    course_name         = serializers.CharField(max_length=20)
    course_description  = serializers.CharField(max_length=200)
    faculty_id          = serializers.IntegerField()
    date_created        = serializers.DateTimeField(read_only=True)
    date_modified       = serializers.DateTimeField(read_only=True)
    lessons             = BulkLessonSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = [
            'id',
            'course_name',
            'course_description',
            'faculty_id',
            'date_created',
            'date_modified',
            'lessons'
        ]


class BulkCategorySerializer(serializers.ModelSerializer):
    """
    Category Serializer fro Category Model
    """
    id                  = serializers.IntegerField(required=False, read_only=True)
    category_name       = serializers.CharField(max_length=200)
    date_created        = serializers.DateTimeField(read_only=True)
    date_modified       = serializers.DateTimeField(read_only=True)
    courses             = BulkCourseSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = [
            'id',
            'category_name',
            'date_created',
            'date_modified',
            'courses'
        ]
