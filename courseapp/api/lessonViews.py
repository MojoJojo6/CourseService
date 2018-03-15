"""
TODO user authentication
TODO response formatting
"""

"""
Refer to doc.org file for documentation of this code.
"""

from rest_framework import generics
from courseapp.models import Lesson
from .lessonSerializers import LessonSerializerCUD, LessonSerializerR


class LessonRUDView(generics.RetrieveUpdateDestroyAPIView):
    """
    Perform Read/Update/Delete operations on Lesson table

    LOOKUP BY `lid` (by default)
    """
    queryset = Lesson.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return LessonSerializerR
        elif self.request.method == "PUT" or "PATCH" or "DELETE":
            return LessonSerializerCUD


class LessonList(generics.ListAPIView):
    serializer_class = LessonSerializerR

    def get_queryset(self):
        queryset = Lesson.objects.all()
        """
        Get list of all the lessons (irrespective of course)
        """
        return Lesson.objects.all()


class LessonCreate(generics.CreateAPIView):
    """
    Create a new Lesson

    All fields required except the `course_id` and `lesson_seqnum`
    """
    serializer_class = LessonSerializerCUD
    queryset = Lesson.objects.all()