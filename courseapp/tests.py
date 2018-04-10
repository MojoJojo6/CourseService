# from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

class Utils():
    @staticmethod
    def testCreateCategory(case):
        url = reverse("courseapp:cat-create")
        data = {
            "cat_name": "test",
            "cat_desc": "made for testing",
            "cat_icon_url": "http://someurl.com"
        }
        response = case.client.post(url, data, format='json')
        case.assertEqual(response.status_code, status.HTTP_201_CREATED)
        print("PASS, test_create_new_category")

    @staticmethod
    def testCreateCourse(case):
        url = reverse("courseapp:course-create")  # namespace:viewName ref[1]
        data = {
            "course_name": "testing",
            "course_description": "testing testing fun",
            "course_icon_url": "http://myimage.com/testing.jpeg",
            "category": 1,
            "faculty": 1
        }
        response = case.client.post(url, data, format='json')
        case.assertEqual(response.status_code, status.HTTP_201_CREATED)
        print("PASS, test_create_new_course")

    @staticmethod
    def testCreateLesson(case):
        url = reverse("courseapp:lesson-create")  # namespace:viewName ref[1]
        data = {
            "course": 1,
            "lesson_name": "test lesson",
            "lesson_seqnum": 1,
            "lesson_desc": "testing is fun",
            "lesson_icon_url": "http://someicon.com/url.jpeg"
        }
        response = case.client.post(url, data, format='json')
        # making sure that course is created successfully
        case.assertEqual(response.status_code, status.HTTP_201_CREATED)
        print("PASS, test_create_new_lesson")

class CategoryCreationAPITestCase(APITestCase):
    def test_create_new_category(self):
        """
        :return:
        """
        response = Utils.testCreateCategory(self)


class CourseCreationAPITestCase(APITestCase):

    def setUp(self):
        """
        create a category
        :return:
        """
        Utils.testCreateCategory(self)

    def test_create_new_course(self):
        """
        :return:
        """
        Utils.testCreateCourse(self)

class LessonCreationAPITest(APITestCase):
    def setUp(self):
        """
        Create a category and a course associated with it.
        :return:
        """
        # create a category
        Utils.testCreateCategory(self)

        # create a course
        Utils.testCreateCourse(self)

    def test_create_new_lesson(self):
        """
        create a new lesson.
        :return:
        """
        Utils.testCreateLesson(self)


class LitemCreationAPITest(APITestCase):
    def setUp(self):
        Utils.testCreateCategory(self)
        Utils.testCreateCourse(self)
        Utils.testCreateLesson(self)

    def test_create_new_litem(self):
        url = reverse("courseapp:litem-create")  # namespace:viewName ref[1]
        data = {
            "lesson": 1,
            "litem_name": "test litem",
            "litem_seqnum": 1,
            "litem_icon_url": "http://justfun.com/a.jpeg",
            "litem_asset_url": "http://somefunny.com/",
            "litem_desc": "testing testing fun"
        }
        response = self.client.post(url, data, format='json')
        # making sure that course is created successfully
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        print("PASS, test_create_new_litem")

class CourseBulkRetrievalTest(APITestCase):
    def setUp(self):
        Utils.testCreateCategory(self)
        Utils.testCreateCourse(self)
        Utils.testCreateCourse(self)

    def test_bulk_course_retrieval(self):
        url = reverse("courseapp:course-bulk-retrieve")
        data = {
            "list": [1, 2]
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print("PASS, test_bulk_course_retrieval")
#     def test_retrieve_course_by_cid(self):
#         """
#         Fetch course details by `cid`
#         :return:
#         """
#
#         # url for retrieving course details for course with cid=9
#         url = reverse("courseapp:course-rud", kwargs={'pk': 1})
#         response = self.client.get(url)
#
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#         # checking if response data is as expected
#         self.assertDictEqual(response.data, {'lessons': [],
#                                               'faculty': None,
#                                               'course_name': 'test course 0',
#                                               'course_description': 'test course for testing',
#                                               'cid': 1,
#                                               'date_modified' : response.data['date_modified'],
#                                               'date_created' : response.data['date_created']})
#
#         pass
#
#     def test_update_course(self):
#         pass
#
#
# # ref
# # [1] https://github.com/encode/django-rest-framework/pull/1143/files/1854f26b5d5ac740201756593a2be01b5c5477d2#diff-5ee455e6a1f5b0502efd536d4bbcf2d8
