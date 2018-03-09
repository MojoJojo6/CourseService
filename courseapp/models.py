from django.db import models


class Litem(models.Model):
    """
    Lesson item model
    """
    liid = models.BigAutoField(primary_key=True)
    # lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=True, blank=True)
    litem_name = models.CharField(max_length=50)
    litem_seqnum = models.IntegerField(null=True)
    litem_desc = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.litem_name

    def __str__(self):
        return "{} / ({}) {}_{}".format(self.litem_seqnum, self.liid, self.litem_name)


class Lesson(models.Model):
    """
     Lesson in Course model
    """
    lid = models.BigAutoField(primary_key=True)
    # course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
    lesson_name = models.CharField(max_length=50)
    lesson_seqnum = models.IntegerField(null=True)
    lesson_desc = models.CharField(max_length=200)

    litems = models.ManyToManyField(Litem)

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.lesson_name

    def __str__(self):
        return "{} / ({}) {}_{}".format(self.litems, self.lesson_seqnum, self.lid, self.lesson_name)


class Course(models.Model):
    """
    Course table for course service
    """
    cid = models.BigAutoField(primary_key=True)
    course_name = models.CharField(max_length=50)
    course_description = models.CharField(max_length=200)
    faculty = models.BigIntegerField(null=True, blank=True)

    lessons = models.ManyToManyField(Lesson)

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.course_name

    def __str__(self):
        return "{}_{}".format(self.cid, self.course_name)


