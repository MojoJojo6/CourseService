from django.db import models


class Litem(models.Model):
    """
    Lesson item model

    Queryset
    {
        liid:   ,
        litem_name: ,
        litem_seqnum:   ,
        litem_desc: ,
        date_created: ,
        date_modified:
    }
    """
    liid = models.BigAutoField(primary_key=True)
    litem_name = models.CharField(max_length=50)
    litem_seqnum = models.IntegerField(null=True)
    litem_desc = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.litem_name

    def __str__(self):
        return "({})_{}_{}".format(self.litem_seqnum, self.liid, self.litem_name)


class Lesson(models.Model):
    """
     Lesson in Course model

     Queryset
     {
        lid: ,
        lesson_name: ,
        lesson_seqnum: ,
        lesson_desc: ,
        litems:[],
        date_created: ,
        date_modified:
     }
    """
    lid = models.BigAutoField(primary_key=True)
    lesson_name = models.CharField(max_length=50)
    lesson_seqnum = models.IntegerField(null=True)
    lesson_desc = models.CharField(max_length=200)
    litems = models.ManyToManyField(Litem)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.lesson_name

    def __str__(self):
        return "({})_{}_{}".format(self.lesson_seqnum, self.lid, self.lesson_name)


class Course(models.Model):
    """
    Course table for course service

    Queryset
    {
        cid: ,
        course_name: ,
        course_description: ,
        faculty: ,
        lessons:[],
        date_created: ,
        date_modified:
    }
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
