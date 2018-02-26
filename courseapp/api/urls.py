from django.conf.urls import url
from .views import CourseRUDView, CourseCreate, CourseList
from django.urls import path
app_name = 'courseapp'

urlpatterns = [
    url(r'^(?P<pk>\d+)/', CourseRUDView.as_view(), name='course-rud'),
    url(r'^create/$', CourseCreate.as_view(), name='course-create'),
    url(r'^$', CourseList.as_view(), name='course-list'),
]