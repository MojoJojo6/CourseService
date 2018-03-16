from rest_framework import serializers
from courseapp.models import Lesson, Litem


class LitemSerializerCUD(serializers.ModelSerializer):
    """
    Serializer to create and update a `litem`.

    Uses `Litem` model.

    `lesson` field is part of `Lesson` model which contains
    manyToMany related field called `litems` to associate
    multiple `litems` with a `Lesson`.

    `lesson` field allows a user to associate a `litem` with
    a `lesson` during creation of that `lesson`.
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
        Method to create a new `litem`.

        Also responsible for adding the created `litem` to `litems`
        field in `Lesson` model.
        """
        lesson = validated_data.pop("lesson")
        litem = Litem(**validated_data)
        litem.save()
        lesson.litems.add(litem)
        return litem

    def update(self, instance, validated_data):
        """
        Method for `litem` updation.

        On each call, it will first check if target `litem`
        exists in any `lesson` in `Lesson` model, if true then `litem`
        will be dissociated from that `lesson` and updated `litem` will be
        added to `lesson` defined in update. All steps will happen irrespective of
        value of `lesson` field.

        :return: instance
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
    Serializer for `Litem` retrieval.

    Uses `Litem` model.
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
