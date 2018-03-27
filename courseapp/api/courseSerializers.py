from rest_framework import serializers
from courseapp.models import Course
from .lessonSerializers import LessonSerializerR
from courseapp.models import Category


class CourseSerializerR(serializers.ModelSerializer):
    """
    Serializer for data retrieval and deletion from `course` model.
    """
    cid = serializers.IntegerField(required=False, read_only=True)
    course_name = serializers.CharField(required=True, max_length=50)
    course_description = serializers.CharField(max_length=200)
    faculty = serializers.IntegerField(required=False, allow_null=True)
    lessons = LessonSerializerR(many=True)
    date_created = serializers.DateTimeField(read_only=True)
    date_modified = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Course
        fields = [
            'cid',
            'course_name',
            'course_description',
            'faculty',
            'lessons',
            'date_created',
            'date_modified',
        ]


class CourseSerializerCUD(serializers.ModelSerializer):
    """
    Serializer for data creation and updation on `Course` model.

    {
        "course_name": "",
        "course_description": "",
        "faculty": null
    }
    """
    cid = serializers.IntegerField(required=False, read_only=True)
    course_name = serializers.CharField(required=True, max_length=50)
    course_description = serializers.CharField(max_length=200)
    category = serializers.ChoiceField(choices=Category.objects.all(), required=True, write_only=True)
    faculty = serializers.IntegerField(required=False, allow_null=True)
    date_created = serializers.DateTimeField(read_only=True)
    date_modified = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Course
        fields = [
            'cid',
            'course_name',
            'course_description',
            'category',
            'faculty',
            'date_created',
            'date_modified',
        ]

    def create(self, validated_data):
        """
        Method for `course` creation.

        Also responsible for adding the created `course` to `courses`
        field in `Category` model.
        """
        category = validated_data.pop("category")
        course = Course(**validated_data)
        course.save()
        category.courses.add(course)
        return course

    def update(self, instance, validated_data):
        """
        Method for `course` updation.

        On each call, it will first check if target `course`
        exists in any `category` in `Category` model, if true then `course`
        will be dissociated from that `Category` and updated `course` will be
        added to `Category` defined in update. All steps will happen irrespective of
        value of `category`(even if `category` is changed) field.

        :return: instance
        """
        # update course
        instance.course_name = validated_data.get('course_name', instance.course_name)
        instance.course_description = validated_data.get('course_description', instance.course_description)
        instance.faculty = validated_data.get('faculty', instance.faculty)
        instance.save()

        # check if associated with an old category
        old_category = Category.objects.filter(courses=instance)
        if len(old_category) == 1:
            # dissociate course from old category
            old_category[0].courses.remove(instance)

        # associate course with new selected category
        new_category = validated_data['category']
        new_category.courses.add(instance)

        return instance
