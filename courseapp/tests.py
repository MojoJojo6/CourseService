# from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
#
from .models import Course
from .api.courseViews import CourseCView

# TODO don't allow courses with same name taught by same faculty
# TODO create a faculty member and add it to course
# TODO update a course details
# TODO delete a course
# TODO get list of courses

import json
import time
class CourseCreationAPITestCase(APITestCase):

    def test_create_new_course(self):
        """
        create 100 distinct courses
        :return:
        """
        url = reverse("courseapp:course-create")  # namespace:viewName ref[1]
        for i in range(10):
            data = {'course_name': 'test course {}'.format(i), 'course_description': "test course for testing"}
            response = self.client.post(url, data, format='json')
            # time.sleep(2)
            # print(response.data)
            # making sure that course is created successfully
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        print("PASS, test_create_of_course")


class CourseRetrievalAPITestCase(APITestCase):
    def setUp(self):
        """
        create 100 distinct courses
        :return:
        """
        url = reverse("courseapp:course-create")  # namespace:viewName ref[1]
        for i in range(100):
            data = {'course_name': 'test course {}'.format(i), 'course_description': "test course for testing"}
            response = self.client.post(url, data, format='json')
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_fetch_list_of_courses(self):
        """
        Fetch list of all the courses
        :return:
        """
        url = reverse("courseapp:course-list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # checking the total count of courses created
        self.assertEqual(len(response.data), 100)

        print("PASS, test_fetch_list_of_courses")

    def test_retrieve_course_by_cid(self):
        """
        Fetch course details by `cid`
        :return:
        """

        # url for retrieving course details for course with cid=9
        url = reverse("courseapp:course-rud", kwargs={'pk': 1})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # checking if response data is as expected
        self.assertDictEqual(response.data, {'lessons': [],
                                              'faculty': None,
                                              'course_name': 'test course 0',
                                              'course_description': 'test course for testing',
                                              'cid': 1,
                                              'date_modified' : response.data['date_modified'],
                                              'date_created' : response.data['date_created']})

        pass

    def test_update_course(self):
        pass


# ref
# [1] https://github.com/encode/django-rest-framework/pull/1143/files/1854f26b5d5ac740201756593a2be01b5c5477d2#diff-5ee455e6a1f5b0502efd536d4bbcf2d8
