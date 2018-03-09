from .models import Course
from .models import Lesson
from .models import Litem

# deleting all courses, lessons and lesson_items first
Course.objects.all().delete()
Lesson.objects.all().delete()
Litem.objects.all().delete()

course_fixtures1 = {
    'course_name':'ML',
    'course_description':'machine learning',
    'faculty':12
}

course_fixtures2 = {
    'course_name':'DM',
    'course_description':'data mining',
    'faculty':17
}

Course.objects.create(**course_fixtures1)
Course.objects.create(**course_fixtures2)

lesson_fixtures1 = {
    'lesson_name':'Clustering',
    'lesson_desc':'Clustering is a form of unsupervised learning'
}

lesson_fixtures2 = {
    'lesson_name':'Regression',
    'lesson_desc':'Regression is a form of supervised learning'
}

lesson1 = Lesson(**lesson_fixtures1)
lesson1.save()

lesson2 = Lesson(**lesson_fixtures2)
lesson2.save()


litem_fixtures1 = {
    'litem_name':'Introduction',
    'litem_desc':'Introduction to the concept of clustering'
}

litem_fixtures2 = {
    'litem_name':'Conclusion',
    'litem_desc':'Concluding concepts'
}

litem1 = Litem(**litem_fixtures1)
litem1.save()

litem2 = Litem(**litem_fixtures2)
litem2.save()
