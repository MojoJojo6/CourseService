from django.db import models

# Create your models here.
class Course(models.Model):
    """
    Course table for course service
    """
    cid = models.BigAutoField(primary_key=True)
    course_name = models.CharField(max_length=50)
    course_description = models.CharField(max_length=200)
    faculty_id = models.BigIntegerField()#uid of Faculty
    date_created = models.DateTimeField(auto_now=True,auto_now_add=False)
    date_modified = models.DateTimeField(auto_now=True,auto_now_add=False)

    def __unicode__(self):
        return self.course_name

    def __str__(self):
        return self.course_name

class Lesson(models.Model):
    """
     Lesson in Course model
    """
    lid = models.BigAutoField(primary_key=True)
    my_course = models.ForeignKey(Course, on_delete=models.CASCADE)
    lesson_name = models.CharField(max_length=50)
    lesson_seqname = models.IntegerField()
    lesson_description = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now=True, auto_now_add=False)
    date_modified = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __unicode__(self):
        return self.lesson_name

    def __str__(self):
        return self.lesson_name


class Lessons_item(models.Model):
    """
    Lesson item model
    """
    lid = models.BigAutoField(primary_key=True)
    my_course = models.ForeignKey(Course, on_delete=models.CASCADE)
    my_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    lesson_item_name = models.CharField(max_length=50)
    lesson_item_seqname = models.IntegerField()
    lesson_item_description = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now=True, auto_now_add=False)
    date_modified = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __unicode__(self):
        return self.lesson_item_name

    def __str__(self):
        return self.lesson_item_name