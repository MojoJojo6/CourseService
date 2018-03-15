"""
Refer to doc.org file for documentation of this code.
"""

from rest_framework import serializers
from courseapp.models import Lesson, Litem


class LitemSerializerCUD(serializers.ModelSerializer):
    """
    Serializer for creation and updation of `litem`
    """
    liid = serializers.IntegerField(required=False, read_only=True)
    litem_name = serializers.CharField(max_length=20)
    litem_seqnum = serializers.IntegerField()
    litem_desc = serializers.CharField(max_length=200)
    lesson = serializers.ChoiceField(choices=Lesson.objects.all(), required=True, write_only=True)
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

    def create(self, validated_data):
        """
        create new litem and add it to the associated lesson's litem list.
        :param validated_data:
        :return:
        """
        lesson = validated_data.pop("lesson")
        litem = Litem(**validated_data)
        litem.save()
        lesson.litems.add(litem)
        return litem

    def create(self, validated_data):
        """
        for data creation
        :param validated_data:
        :return:
        """
        # for creation
        course = validated_data.pop("course")
        lesson = Lesson(**validated_data)
        lesson.save()
        course.lessons.add(lesson)
        return lesson

    def update(self, instance, validated_data):
        """
        For `litem` updation.

        It will first check if the litem exists in any present lesson,
        if true then the litem will be dissociated from that lesson.

        It will add litem to the defined lesson.
        :return:
        """
        # update lesson
        instance.litem_name = validated_data.get('lesson_name', instance.litem_name)
        instance.litem_seqnum = validated_data.get('lesson_seqnum', instance.litem_seqnum)
        instance.litem_desc = validated_data.get('lesson_desc', instance.litem_desc)
        instance.save()

        # check if associated with an old lesson
        old_lesson = Lesson.objects.filter(litems=instance)
        if len(old_lesson) == 1:
            # dissociate litem from old lesson
            old_lesson[0].litems.remove(instance)

        # associate litem with new selected lesson
        new_lesson = validated_data['lesson']
        new_lesson.litems.add(instance)
        return instance


class LitemSerializerR(serializers.ModelSerializer):
    """
    Serializer for `litem` retrieval and deletion
    """
    liid = serializers.IntegerField(required=False, read_only=True)
    litem_name = serializers.CharField(max_length=20)
    litem_seqnum = serializers.IntegerField()
    litem_desc = serializers.CharField(max_length=200)
    date_created = serializers.DateTimeField(read_only=True)
    date_modified = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Litem
        fields = [
            'liid',
            'litem_name',
            'litem_seqnum',
            'litem_desc',
            'date_created',
            'date_modified'
        ]