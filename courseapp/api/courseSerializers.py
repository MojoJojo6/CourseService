from rest_framework import serializers
from courseapp.models import Course
from .lessonSerializers import LessonSerializerR
from courseapp.models import Category


class CourseSerializerR(serializers.ModelSerializer):
    """
    Serializer for data retrieval from `course` model.
    """
    cid = serializers.IntegerField(required=False, read_only=True)
    course_name = serializers.CharField(required=True, max_length=50)
    course_description = serializers.CharField(max_length=200)
    course_icon_url = serializers.URLField(max_length=200, allow_null=True, required=False)
    faculty = serializers.IntegerField(required=False, allow_null=True)
    lessons = LessonSerializerR(many=True, read_only=True)
    date_created = serializers.DateTimeField(read_only=True)
    date_modified = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Course
        fields = [
            'cid',
            'course_name',
            'course_description',
            'course_icon_url',
            'faculty',
            'lessons',
            'date_created',
            'date_modified',
        ]


class CourseSerializerCUD(serializers.ModelSerializer):
    """
    Serializer for data creation and updation on `Course` model.

    {
        "course_name": "",
        "course_description": "",
        "faculty": null
    }
    """
    cid = serializers.IntegerField(required=False, read_only=True)
    course_name = serializers.CharField(required=True, max_length=50)
    course_description = serializers.CharField(max_length=200)
    course_icon_url = serializers.URLField(max_length=200, allow_null=True, required=False)
    faculty = serializers.IntegerField(required=False, allow_null=True)
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    date_created = serializers.DateTimeField(read_only=True)
    date_modified = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Course
        fields = [
            'cid',
            'course_name',
            'course_description',
            'course_icon_url',
            'category',
            'faculty',
            'date_created',
            'date_modified',
        ]

class CourseSerializerBulkR(serializers.ModelSerializer):
    """
    Serializer for data retrieval from `course` model.
    """
    cid = serializers.IntegerField(required=True)
    course_name = serializers.CharField(read_only=True)
    course_description = serializers.CharField(max_length=200, read_only=True)
    course_icon_url = serializers.URLField(read_only=True)
    faculty = serializers.IntegerField(required=False, allow_null=True, read_only=True)
    lessons = LessonSerializerR(many=True, read_only=True)
    date_created = serializers.DateTimeField(read_only=True)
    date_modified = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Course
        fields = [
            'cid',
            'course_name',
            'course_description',
            'course_icon_url',
            'faculty',
            'lessons',
            'date_created',
            'date_modified',
        ]