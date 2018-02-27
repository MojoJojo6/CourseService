from rest_framework import serializers
from courseapp.models import Course, Lesson

class CourseSerializer(serializers.ModelSerializer):
    """
    Serializer for `Course` model

    Each course has only one faculty associated with it.

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
    Serializer for `Lesson` model

    Each lesson is related to only one course
    and has only one unique sequence number

    TODO make course_id and lesson_seqnum optional
    """
    lid = serializers.IntegerField(required=False,read_only=True)
    course_id = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all())
    lesson_name = serializers.CharField(max_length=20)
    lesson_seqnum = serializers.IntegerField()
    lesson_desc = serializers.CharField(max_length=200)
    date_created = serializers.DateTimeField(read_only=True)
    date_modified = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Lesson
        fields = [
            'lid',
            'course_id',
            'lesson_name',
            'lesson_seqnum',
            'lesson_desc',
            'date_created',
            'date_modified',
        ]