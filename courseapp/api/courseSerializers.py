from rest_framework import serializers
from courseapp.models import Course
from .lessonSerializers import LessonSerializerCUD, LessonSerializerR

class CourseSerializerRD(serializers.ModelSerializer):
    """
    Serializer for `Course` model retrieval and deletion.
    """
    cid = serializers.IntegerField(required=False, read_only=True)
    course_name = serializers.CharField(required=True, max_length=50)
    course_description = serializers.CharField(max_length=200)
    faculty = serializers.IntegerField(required=False, allow_null=True)
    lessons = LessonSerializerR(many=True)
    date_created = serializers.DateTimeField(read_only=True)
    date_modified = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Course
        fields = [
            'cid',
            'course_name',
            'course_description',
            'faculty',
            'lessons',
            'date_created',
            'date_modified',
        ]


class CourseSerializerCU(serializers.ModelSerializer):
    """
    Serializer for `Course` model creation and updation.
    """
    cid = serializers.IntegerField(required=False, read_only=True)
    course_name = serializers.CharField(required=True, max_length=50)
    course_description = serializers.CharField(max_length=200)
    faculty = serializers.IntegerField(required=False, allow_null=True)
    date_created = serializers.DateTimeField(read_only=True)
    date_modified = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Course
        fields = [
            'cid',
            'course_name',
            'course_description',
            'faculty',
            'date_created',
            'date_modified',
        ]