from ..models import Course
from ..models import Lesson
from ..models import Lessons_item
from rest_framework import serializers

class CourseSerializer(serializers.ModelSerializer):
    """
    Serializer for Course Model
    """
    cid = serializers.IntegerField(required=False,read_only=True)
    course_name = serializers.CharField(max_length=20)
    course_description = serializers.CharField(max_length=200)
    faculty_id = serializers.IntegerField()
    date_created = serializers.DateTimeField(read_only=True)
    date_modified = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Course
        fields = ['cid','course_name','course_description','faculty_id']

class LessonSerializer(serializers.ModelSerializer):
    """
    Serializer for Lesson Model
    """
    lid = serializers.IntegerField(required=False,read_only=True)
    my_course = CourseSerializer(many=True)
    lesson_name = serializers.CharField(max_length=20)
    lesson_seqname = serializers.IntegerField()
    lesson_description = serializers.CharField(max_length=200)
    date_created = serializers.DateTimeField(read_only=True)
    date_modified = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Course
        fields = ['lid','my_course','lesson_name','lesson_seqname','lesson_description']

class Lesson_itemSerializer(serializers.ModelSerializer):
    """
    Serializer for Lesson Item Model
    """
    lid = serializers.IntegerField(required=False, read_only=True)
    my_course = CourseSerializer(many=True)
    my_lesson = LessonSerializer(many=True)
    lesson_item_name = serializers.CharField(max_length=20)
    lesson_item_seqname = serializers.IntegerField()
    lesson_item_description = serializers.CharField(max_length=200)
    date_created = serializers.DateTimeField(read_only=True)
    date_modified = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Course
        fields = ['lid','my_course','my_lesson','lesson_item_name','lesson_item_seqname','lesson_item_description']



