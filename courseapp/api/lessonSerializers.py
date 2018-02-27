from rest_framework import serializers
from courseapp.models import Course, Lesson

class LessonSerializer(serializers.ModelSerializer):
    """
    Serializer for `Lesson` model

    Each lesson is related to only one course
    and has only one unique sequence number
    """
    lid = serializers.IntegerField(required=False,read_only=True)
    course_id = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all(), allow_null=True, required=False)
    lesson_name = serializers.CharField(max_length=20)
    lesson_seqnum = serializers.IntegerField(allow_null=True, required=False)
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