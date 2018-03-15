from rest_framework import serializers
from courseapp.models import Course, Lesson
from .litemSerializers import LitemSerializerR


class LessonSerializerR(serializers.ModelSerializer):
    """
    Serializer for `Lesson` model

    Each lesson is related to only one course
    and has only one unique sequence number
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
    Serializer for `Lesson` model

    Each lesson is related to only one course
    and has only one unique sequence number
    """
    lid = serializers.IntegerField(required=False,read_only=True)
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
        For `lesson` updation.

        It will first check if the lesson exists in any present course,
        if true then the lesson will be dissociated from that course.

        It will add lesson to the defined course.
        :return:
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

