from rest_framework import serializers
from courseapp.models import Course, Lesson
from .litemSerializers import LitemSerializerR


class LessonSerializerR(serializers.ModelSerializer):
    """
    Serializer for `Lesson` retrieval.

    Uses `Lesson` model.

    The `litems` field is a `manyToMany` relation field which is associated
    with `LitemSerializerR` serializer class.
    """
    lid = serializers.IntegerField(required=False,read_only=True)
    litems = LitemSerializerR(many=True)
    lesson_name = serializers.CharField(max_length=20)
    lesson_seqnum = serializers.IntegerField(allow_null=True, required=False)
    lesson_desc = serializers.CharField(max_length=200)
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
            'date_created',
            'date_modified',
        ]


class LessonSerializerCUD(serializers.ModelSerializer):
    """
    Serializer for `Lesson` creation, updation, deletion.

    Uses `Lesson` model.

    `course` field is part of `Course` model which contains
    manyToMany related field called `lessons` to associate
    multiple `lessons` with a `Course`.

    `course` field allows a user to associate a `lesson` with
    a `course` during creation of that `lesson`.
    """
    lid = serializers.IntegerField(required=False, read_only=True)
    course = serializers.ChoiceField(choices=Course.objects.all(), required=True, write_only=True)
    lesson_name = serializers.CharField(max_length=20)
    lesson_seqnum = serializers.IntegerField(allow_null=True, required=False)
    lesson_desc = serializers.CharField(max_length=200)
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
            'date_created',
            'date_modified',
        ]

    def create(self, validated_data):
        """
        Method for `lesson` creation.

        Also responsible for adding the created `lesson` to `lessons`
        field in `Course` model.
        """
        course = validated_data.pop("course")
        lesson = Lesson(**validated_data)
        lesson.save()
        course.lessons.add(lesson)
        return lesson

    def update(self, instance, validated_data):
        """
        Method for `lesson` updation.

        On each call, it will first check if target `lesson`
        exists in any `course` in `Course` model, if true then `lesson`
        will be dissociated from that `course` and updated `lesson` will be
        added to `course` defined in update. All steps will happen irrespective of
        value of `course` field.

        :return: instance
        """
        # update lesson
        instance.lesson_name = validated_data.get('lesson_name', instance.lesson_name)
        instance.lesson_seqnum = validated_data.get('lesson_seqnum', instance.lesson_seqnum)
        instance.lesson_desc = validated_data.get('lesson_desc', instance.lesson_desc)
        instance.save()

        # check if associated with an old course
        old_course = Course.objects.filter(lessons=instance)
        if len(old_course) == 1:
            # dissociate lesson from old course
            old_course[0].lessons.remove(instance)

        # associate lesson with new selected course
        new_course = validated_data['course']
        new_course.lessons.add(instance)

        return instance

