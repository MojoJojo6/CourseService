"""
Refer to doc.org file for documentation of this code.
"""

from rest_framework import serializers
from courseapp.models import Lesson, Litem
from .lessonSerializers import LessonSerializer

class LitemSerializer(serializers.ModelSerializer):
    """
    Serializer for Lesson Item Model
    """
    liid = serializers.IntegerField(required=False, read_only=True)
    # lesson = serializers.PrimaryKeyRelatedField(queryset=Lesson.objects.all(), allow_null=True, required=False)

    lessons = LessonSerializer(many=True)

    litem_name = serializers.CharField(max_length=20)
    litem_seqnum = serializers.IntegerField()
    litem_desc = serializers.CharField(max_length=200)
    date_created = serializers.DateTimeField(read_only=True)
    date_modified = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Litem
        fields = [
            'liid',
            'lesson',
            'litem_name',
            'litem_seqnum',
            'litem_desc',
            'date_created',
            'date_modified'
        ]