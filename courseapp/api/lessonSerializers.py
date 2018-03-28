from rest_framework import serializers
from courseapp.models import Course, Lesson
from .litemSerializers import LitemSerializerR


class LessonSerializerR(serializers.ModelSerializer):
    """
    Serializer for `Lesson` retrieval.

    Uses `Lesson` model.

    The `litems` field is associated
    with `LitemSerializerR` serializer class.
    """
    lid = serializers.IntegerField(required=False,read_only=True)
    litems = LitemSerializerR(many=True, read_only=True)
    lesson_name = serializers.CharField(max_length=20)
    lesson_seqnum = serializers.IntegerField(allow_null=True, required=False)
    lesson_desc = serializers.CharField(max_length=200)
    lesson_icon_url = serializers.URLField(max_length=200, allow_null=True, required=False)
    date_created = serializers.DateTimeField(read_only=True)
    date_modified = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Lesson
        fields = [
            'lid',
            'litems',
            'lesson_name',
            'lesson_seqnum',
            'lesson_desc',
            'lesson_icon_url',
            'date_created',
            'date_modified',
        ]


class LessonSerializerCUD(serializers.ModelSerializer):
    """
    Serializer for `Lesson` creation, updation, deletion.

    Uses `Lesson` model.

    `course` field is part of `Course` model which is a foreign key
    in `lesson` model.

    """
    lid = serializers.IntegerField(required=False, read_only=True)
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all())
    lesson_name = serializers.CharField(max_length=20)
    lesson_seqnum = serializers.IntegerField(allow_null=True, required=False)
    lesson_desc = serializers.CharField(max_length=200)
    lesson_icon_url = serializers.URLField(max_length=200, allow_null=True, required=False)
    date_created = serializers.DateTimeField(read_only=True)
    date_modified = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Lesson
        fields = [
            'lid',
            'course',
            'lesson_name',
            'lesson_seqnum',
            'lesson_desc',
            'lesson_icon_url',
            'date_created',
            'date_modified',
        ]
