from django.db import models

class Course(models.Model):
    """
    Course table for course service
    """
    cid = models.BigAutoField(primary_key=True)
    course_name = models.CharField(max_length=50)
    course_description = models.CharField(max_length=200)
    faculty_id = models.BigIntegerField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.course_name

    def __str__(self):
        return "{} - {}".format(self.cid, self.course_name)


class Lesson(models.Model):
    """
     Lesson in Course model
    """
    lid = models.BigAutoField(primary_key=True)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
    lesson_name = models.CharField(max_length=50)
    lesson_seqnum = models.IntegerField(null=True, blank=True)
    lesson_desc = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.lesson_name

    def __str__(self):
        return "{} - {}".format(self.lid, self.lesson_name)