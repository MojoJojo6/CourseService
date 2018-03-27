from rest_framework import generics
from courseapp.models import Course
from .courseSerializers import CourseSerializerR, CourseSerializerCUD


class CourseCView(generics.CreateAPIView):
    """
    View to create a new `course`.

    Uses `CourseSerializerCU` serializer class.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializerCUD


class CourseRUDView(generics.RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update and delete a `course`.

    Uses `CourseRDSerializer` serializer class for `course`
    retrieval, deletion and `CourseCUSerializer` serializer
    class for updating a `course`.
    """
    queryset = Course.objects.all()

    def get_serializer_class(self):
        request_method = self.request.method

        if request_method == "GET":
            return CourseSerializerR

        elif request_method == "PATCH" or "PUT":
            return CourseSerializerCUD

        elif request_method == "DELETE":
            return CourseSerializerCUD


class CourseListView(generics.ListAPIView):
    """
    View to get list of `course`.

    Uses `CourseSerializerRD` serializer class.
    """
    serializer_class = CourseSerializerR
    queryset = Course.objects.all()