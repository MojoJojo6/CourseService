"""
TODO user authentication
TODO response formatting
"""

"""
Course:
- create: all fields required except faculty(optional)
- retrieve: lookup_field = 'cid'
- retrieve: list of courses
- update: lookup_field = 'cid'
- delete: lookup_field = 'cid'

Lesson:
- create: all fields required
- delete:
"""

from rest_framework import generics, mixins
from courseapp.models import Course
from .serializers import CourseSerializer

class CourseRUDView(generics.RetrieveUpdateDestroyAPIView):
    """
    Read/Update/Delete operation on Course table

    LOOKUP BY `cid`
    """
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class CourseCreate(generics.CreateAPIView):
    """
    Create new course

    All fields required except `faculty_id`,
    so the instructor of the course could be decided later.
    """
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

class CourseList(generics.ListAPIView):
    """
    Get a list of all the courses
    """
    serializer_class = CourseSerializer
    queryset = Course.objects.all()