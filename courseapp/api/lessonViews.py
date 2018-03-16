from rest_framework import generics
from courseapp.models import Lesson
from .lessonSerializers import LessonSerializerCUD, LessonSerializerR


class LessonRUDView(generics.RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update or delete a `lesson`.

    Uses `LessonSerializerR` serializer class for `lesson` retrieval,
    `LessonSerializerCUD` serializer class to create, update and delete
    a `lesson`.
    """
    queryset = Lesson.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return LessonSerializerR
        elif self.request.method == "PUT" or "PATCH" or "DELETE":
            return LessonSerializerCUD


class LessonList(generics.ListAPIView):
    """
    View to get list of all the `lesson` present in `Lesson` model.

    Uses `LessonSerializerR` serializer class.
    """
    serializer_class = LessonSerializerR
    queryset = Lesson.objects.all()


class LessonCreate(generics.CreateAPIView):
    """
    View to create a new `lesson`.

    Uses `LessonSerializerCUD` serializer class.
    """
    serializer_class = LessonSerializerCUD
    queryset = Lesson.objects.all()