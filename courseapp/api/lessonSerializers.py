from rest_framework import serializers
from courseapp.models import Course, Lesson
from .litemSerializers import LitemSerializer


class LessonSerializer(serializers.ModelSerializer):
    """
    Serializer for `Lesson` model

    Each lesson is related to only one course
    and has only one unique sequence number
    """
    lid = serializers.IntegerField(required=False,read_only=True)
    # course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all(), allow_null=True, required=False)

    litems = LitemSerializer(many=True)

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


class CourseField(serializers.Field):
    """
    course field
    """
    def to_representation(self, value):
        """
        to representation
        :param value:
        :return:
        """
        import ipdb
        ipdb.set_trace()

        return value

    def to_internal_value(self, data):
        """
        convert to internal value
        :param data: data should be a list
        :return:
        """
        import ipdb
        ipdb.set_trace()

        if len(data) > 1:
            raise serializers.ValidationError("The number of courses cannot be more than one")
        return Course.objects.get(cid=data[0][0])


class LessonSerializerCreate(serializers.ModelSerializer):
    """
    Serializer for `Lesson` model

    Each lesson is related to only one course
    and has only one unique sequence number
    """
    lid = serializers.IntegerField(required=False,read_only=True)

    course = serializers.ChoiceField(choices=Course.objects.all(), required=True)

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

    