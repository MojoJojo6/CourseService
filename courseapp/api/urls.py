from django.conf.urls import url
from .views import \
    CourseRUDView, CourseCreate, CourseList, \
    LessonCreate, LessonRUDView, LessonList, LessonListByCourseId, LessonRetrieveByCIDAndLSeqNum
from django.urls import path
app_name = 'courseapp'

# defining strings which are used to categorise endpoints
uri_types = ['courses', 'lessons']

urlpatterns = [
    url(r'^{0}/(?P<pk>\d+)/'.format(uri_types[0]), CourseRUDView.as_view(), name='course-rud'),
    url(r'^{0}/create/$'.format(uri_types[0]), CourseCreate.as_view(), name='course-create'),
    url(r'^{0}/$'.format(uri_types[0]), CourseList.as_view(), name='course-list'),

    url(r'{0}/create/$'.format(uri_types[1]), LessonCreate.as_view(), name='lesson-create'),
    url(r'{0}/(?P<pk>\d+)/$'.format(uri_types[1]), LessonRUDView.as_view(), name='lesson-rud'),
    url(r'{0}/$'.format(uri_types[1]), LessonList.as_view(), name='lesson-list'),
    # url(r'{0}/$'.format(uri_types[1]), LessonListByCourseId.as_view(), name='lesson-list-courseid'),
    # url(r'{0}/(?P<course_id>.+)/(?P<lesson_seqnum>.+)/$'.format(uri_types[1]), LessonRetrieveByCIDAndLSeqNum.as_view(),
    # name='lesson-r-cid-lseqnum')
]
