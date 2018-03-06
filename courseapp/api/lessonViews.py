"""
TODO user authentication
TODO response formatting
"""

"""
Refer to doc.org file for documentation of this code.
"""

from rest_framework import generics
from courseapp.models import Lesson
from .lessonSerializers import LessonSerializer

class LessonRUDView(generics.RetrieveUpdateDestroyAPIView):
    """
    Perform Read/Update/Delete operations on Lesson table

    LOOKUP BY `lid` (by default)
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

class LessonList(generics.ListAPIView):
    serializer_class = LessonSerializer
    def get_queryset(self):
        queryset = Lesson.objects.all()
        query_params = self.request.query_params
        course_id = query_params.get('cid', None)
        lesson_seqnum = query_params.get('seqnum', None)

        if (course_id != None and lesson_seqnum != None):
            """
            Retrieve details of lesson selected by `course_id` and `lesson_seqnum`.

            It is useful when the user wants to jump to a particular lesson in the course playlist.
            """
            return Lesson.objects.filter(course=course_id, lesson_seqnum = lesson_seqnum)
        elif (course_id != None):
            """
            Retrieve list of lessons by `course_id`

            To get the list of all the lessons associated with same course.
            It is useful when user wants to load a course playlist.
            """
            return Lesson.objects.filter(course=course_id)
        else:
            """
            Get list of all the lessons (irrespective of course)
            """
            return Lesson.objects.all()

class LessonCreate(generics.CreateAPIView):
    """
    Create a new Lesson

    All fields required except the `course_id` and `lesson_seqnum`
    """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()