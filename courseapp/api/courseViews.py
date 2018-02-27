
"""
Refer to doc.org file for documentation of this code.
"""

from rest_framework import generics
from courseapp.models import Course
from .courseSerializers import CourseSerializer

class CourseRUDView(generics.RetrieveUpdateDestroyAPIView):
    """
    Perform Read/Update/Delete operation on Course table

    LOOKUP BY `cid` (by default)
    """
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

class CourseCreate(generics.CreateAPIView):
    """
    Create a new course

    All fields required except `faculty_id`,
    so the instructor of the course could be decided later.
    """
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

class CourseList(generics.ListAPIView):
    """
    Get list of all the courses
    """
    serializer_class = CourseSerializer
    queryset = Course.objects.all()