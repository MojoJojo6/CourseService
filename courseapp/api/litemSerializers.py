"""
Refer to doc.org file for documentation of this code.
"""

from rest_framework import serializers
from courseapp.models import Lesson, Litem

class LitemSerializer(serializers.ModelSerializer):
    """
    Serializer for Lesson Item Model
    """
    liid = serializers.IntegerField(required=False, read_only=True)
    lesson_id = serializers.PrimaryKeyRelatedField(queryset=Lesson.objects.all(), allow_null=True, required=False)
    litem_name = serializers.CharField(max_length=20)
    litem_seqname = serializers.IntegerField()
    litem_desc = serializers.CharField(max_length=200)
    date_created = serializers.DateTimeField(read_only=True)
    date_modified = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Litem
        fields = [
            'liid',
            'lesson_id',
            'litem_name',
            'litem_seqname',
            'litem_desc',
            'date_created',
            'date_modified'
        ]