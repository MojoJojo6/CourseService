from django.conf.urls import url
from .courseViews import \
    CourseCView, \
    CourseRUDView, \
    CourseListView, \
    CourseBulkView

from .lessonViews import \
    LessonCreate, \
    LessonRUDView, \
    LessonList

from .litemViews import \
    LitemCreate, \
    LitemList, \
    LitemRUDView

from .categoryView import \
    CategoryCreate, \
    CategoryRUDView, \
    CategoryList

# from django.urls import path

app_name = 'courseapp'

# defining strings which are used to categorise endpoints
uri_types = ['courses', 'lessons', 'litems', 'categories']

urlpatterns = [
    url(r'^{0}/getbulk/$'.format(uri_types[0]), CourseBulkView.as_view(), name='course-bulk-retrieve'),
    url(r'^{0}/create/$'.format(uri_types[0]), CourseCView.as_view(), name='course-create'),
    url(r'{0}/(?P<pk>\d+)/$'.format(uri_types[0]), CourseRUDView.as_view(), name='course-rud'),
    url(r'^{0}/$'.format(uri_types[0]), CourseListView.as_view(), name='course-list'),

    url(r'{0}/create/$'.format(uri_types[1]), LessonCreate.as_view(), name='lesson-create'),
    url(r'{0}/(?P<pk>\d+)/$'.format(uri_types[1]), LessonRUDView.as_view(), name='lesson-rud'),
    url(r'{0}/$'.format(uri_types[1]), LessonList.as_view(), name='lesson-list'),

    url(r'{0}/create/$'.format(uri_types[2]), LitemCreate.as_view(), name='litem-create'),
    url(r'{0}/(?P<pk>\d+)/$'.format(uri_types[2]), LitemRUDView.as_view(), name='litem-rud'),
    url(r'{0}/$'.format(uri_types[2]), LitemList.as_view(), name='litem-list'),

    url(r'{0}/create/$'.format(uri_types[3]), CategoryCreate.as_view(), name='cat-create'),
    url(r'{0}/(?P<pk>\d+)/$'.format(uri_types[3]), CategoryRUDView.as_view(), name='cat-rud'),
    url(r'{0}/$'.format(uri_types[3]), CategoryList.as_view(), name='cat-list'),
]
