
"""
Refer to doc.org file for documentation of this code.
"""

from rest_framework import generics
from courseapp.models import Course
from .courseSerializers import CourseSerializerCU, CourseSerializerRD


class CourseCView(generics.CreateAPIView):
    """
    Create a new course

    All fields required except `faculty_id` and `lessons`
    so the instructor of the course could be decided later
    and lesson will be assigned to course while creation of lesson itself.
    """
    # serializer_class = CourseSerializerCU
    queryset = Course.objects.all()
    serializer_class = CourseSerializerCU


class CourseRUDView(generics.RetrieveUpdateDestroyAPIView):
    """
    Perform Read, Update or Destroy operation on Course table

    LOOKUP BY `cid` (by default)
    """
    queryset = Course.objects.all()

    def get_serializer_class(self):
        request_method = self.request.method

        if request_method == "GET":
            return CourseSerializerRD

        elif request_method == "PATCH" or "PUT":
            return CourseSerializerCU

        elif request_method == "DELETE":
            return CourseSerializerRD


class CourseListView(generics.ListAPIView):
    """
    Get list of all the courses
    """
    serializer_class = CourseSerializerRD
    queryset = Course.objects.all()