from rest_framework import serializers
from courseapp.models import Lesson, Litem


class LitemSerializerCUD(serializers.ModelSerializer):
    """
    Serializer to create and update a `litem`.

    Uses `Litem` model.

    `lesson` field is part of `Lesson` model which is foreign key in `litem`.
    """
    liid = serializers.IntegerField(required=False, read_only=True)
    litem_name = serializers.CharField(max_length=20)
    litem_seqnum = serializers.IntegerField()
    litem_desc = serializers.CharField(max_length=200)
    lesson = serializers.PrimaryKeyRelatedField(queryset=Lesson.objects.all())
    litem_icon_url = serializers.URLField(max_length=200, allow_null=True, required=False)
    litem_asset_url = serializers.URLField(max_length=200, allow_null=True, required=False)
    date_created = serializers.DateTimeField(read_only=True)
    date_modified = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Litem
        fields = [
            'liid',
            'lesson',
            'litem_name',
            'litem_seqnum',
            'litem_icon_url',
            'litem_asset_url',
            'litem_desc',
            'date_created',
            'date_modified'
        ]


class LitemSerializerR(serializers.ModelSerializer):
    """
    Serializer for `Litem` retrieval.

    Uses `Litem` model.
    """
    liid = serializers.IntegerField(required=False, read_only=True)
    litem_name = serializers.CharField(max_length=20)
    litem_seqnum = serializers.IntegerField()
    litem_desc = serializers.CharField(max_length=200)
    date_created = serializers.DateTimeField(read_only=True)
    date_modified = serializers.DateTimeField(read_only=True)
    litem_icon_url = serializers.URLField(max_length=200, allow_null=True, required=False)
    litem_asset_url = serializers.URLField(max_length=200,allow_null=True, required=False)
    class Meta:
        model = Litem
        fields = [
            'liid',
            'litem_name',
            'litem_seqnum',
            'litem_icon_url',
            'litem_asset_url',
            'litem_desc',
            'date_created',
            'date_modified'
        ]
