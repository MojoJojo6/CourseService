from rest_framework import generics, response
from courseapp.models import Course
from .courseSerializers import CourseSerializerR, CourseSerializerCUD, CourseSerializerBulkR
from rest_framework.mixins import CreateModelMixin


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


class CourseBulkView(generics.GenericAPIView):
    """
    View to retrieve a list of courses.

    ! overriding `post` method
    """

    queryset = Course.objects.all()
    serializer_class = CourseSerializerBulkR

    def post(self, request, *args, **kwargs):
        data = self.request.data
        course_objects = []
        for cid in data["list"]:
            course_objects.append(Course.objects.get(cid=cid))
        serializer = self.get_serializer_class()
        return response.Response(data=serializer(course_objects, many=True).data, status=200)