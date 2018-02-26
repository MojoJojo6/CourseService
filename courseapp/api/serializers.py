from rest_framework import serializers
from courseapp.models import Course

class CourseSerializer(serializers.ModelSerializer):
    """
    TODO make faculty_id optional
    """
    cid = serializers.IntegerField(required=False, read_only=True)
    course_name = serializers.CharField(required=True, max_length=50)
    course_description = serializers.CharField(max_length=200)
    faculty_id = serializers.IntegerField()
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

class LessonSerializer(serializers.ModelSerializer):
    """
    Serializer for Lesson Model
    """
    lid = serializers.IntegerField(required=False,read_only=True)
    course_id = CourseSerializer(many=True)
    lesson_name = serializers.CharField(max_length=20)
    lesson_seqnum = serializers.IntegerField()
    lesson_desc = serializers.CharField(max_length=200)
    date_created = serializers.DateTimeField(read_only=True)
    date_modified = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Course
        fields = [
            'lid',
            'course_id',
            'lesson_name',
            'lesson_seqnum',
            'lesson_desc',
        ]