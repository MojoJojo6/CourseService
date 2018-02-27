from django.conf.urls import url
from .courseViews import \
    CourseRUDView, \
    CourseCreate, \
    CourseList
from .lessonViews import \
    LessonCreate, \
    LessonRUDView, \
    LessonList

# from django.urls import path

app_name = 'courseapp'

# defining strings which are used to categorise endpoints
uri_types = ['courses', 'lessons']

urlpatterns = [
    url(r'^{0}/create/$'.format(uri_types[0]), CourseCreate.as_view(), name='course-create'),
    url(r'{0}/(?P<pk>\d+)/$'.format(uri_types[0]), CourseRUDView.as_view(), name='course-rud'),
    url(r'^{0}/$'.format(uri_types[0]), CourseList.as_view(), name='course-list'),

    url(r'{0}/create/$'.format(uri_types[1]), LessonCreate.as_view(), name='lesson-create'),
    url(r'{0}/(?P<pk>\d+)/$'.format(uri_types[1]), LessonRUDView.as_view(), name='lesson-rud'),
    url(r'{0}/$'.format(uri_types[1]), LessonList.as_view(), name='lesson-list'),
]
