from rest_framework import serializers
from courseapp.models import Course, Lesson

class CourseSerializer(serializers.ModelSerializer):
    """
    Serializer for `Course` model

    Each course has only one faculty associated with it.
    """
    cid = serializers.IntegerField(required=False, read_only=True)
    course_name = serializers.CharField(required=True, max_length=50)
    course_description = serializers.CharField(max_length=200)
    faculty_id = serializers.IntegerField(required=False, allow_null=True)
    date_created = serializers.DateTimeField(read_only=True)
    date_modified = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Course
        fields = [
            'cid',
            'course_name',
            'course_description',
            'faculty_id',
            'date_created',
            'date_modified',
        ]