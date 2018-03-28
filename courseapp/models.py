from django.db import models

"""
    Litem points to a lesson, lesson points to a course, course points to a category.
    
    "many ------> one" relationships implemented by using foreign keys.
    
    On deletion of a lesson, all the associated litems will be deleted.
    On deletion of a category, course, all the associated courses and lessons respectively
    will not be deleted.
"""

class Category(models.Model):
    """
    `Category` model

    All fields required except `cat_desc` and `cat_icon_url`.

    :queryset: {
        cat_id (auto generated),
        cat_name (name/title),
        cat_desc (description of max 200 chars),
        cat_icon_url (URL of image or icon which describes the category),
        date_created (auto generated),
        date_modified (auto generated)
    }
    """
    cat_id = models.BigAutoField(primary_key=True)
    cat_name = models.CharField(max_length=50)
    cat_desc = models.CharField(max_length=200, null=True, blank=True)
    cat_icon_url = models.URLField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.cat_name

    def __str__(self):
        return "[{}]".format(self.cat_name)

class Course(models.Model):
    """
    `Course` model.

    All fields are required except `faculty`, `course_icon_url`.

    If you delete a category, the courses associated with it won't be deleted.

    :queryset: {
        cid,
        course_name,
        course_description,
        faculty,
        category (foreign key),
        course_icon_url,
        date_created,
        date_modified
        }
    """
    cid = models.BigAutoField(primary_key=True)
    course_name = models.CharField(max_length=50)
    course_description = models.CharField(max_length=200)
    faculty = models.BigIntegerField(null=True, blank=True)
    category = models.ForeignKey(Category, related_name='courses', on_delete=models.PROTECT)
    course_icon_url = models.URLField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.course_name

    def __str__(self):
        return "{}__{}".format(self.category, self.course_name)


class Lesson(models.Model):
    """
     `Lesson` model.

     All fields are required except `litems`, `lesson_seqnum`.

     If you delete a Course, all the lessons associated with it won't be deleted.

     :queryset: {
        lid,
        lesson_name,
        lesson_seqnum,
        lesson_desc,
        course (foreign key),
        lesson_icon_url,
        date_created,
        date_modified
        }
    """
    lid = models.BigAutoField(primary_key=True)
    lesson_name = models.CharField(max_length=50)
    lesson_seqnum = models.IntegerField(null=True)
    lesson_desc = models.CharField(max_length=200)
    course = models.ForeignKey(Course, related_name='lessons', on_delete=models.PROTECT)
    lesson_icon_url = models.URLField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.lesson_name

    def __str__(self):
        return "{}__{}-{}".format(self.course, self.lesson_seqnum, self.lesson_name)


class Litem(models.Model):
    """
    `LessonItem` model.

    All fields are required except `lesson_seqnum`.

    If you delete a lesson, all the `litems` associated with that lesson will be deleted.

    :queryset: {
        liid,
        litem_name,
        litem_seqnum,
        litem_desc,
        lesson (foreign key),
        litem_icon_url (URL of an icon or image which describes the lesson item),
        litem_asset_url (URL of an asset which represents the content of lesson item),
        date_created,
        date_modified
        }
    """
    liid = models.BigAutoField(primary_key=True)
    litem_name = models.CharField(max_length=50)
    litem_seqnum = models.IntegerField(null=True)
    litem_desc = models.CharField(max_length=200)
    lesson = models.ForeignKey(Lesson, related_name='litems', on_delete=models.CASCADE)
    litem_icon_url = models.URLField(max_length=200, null=True, blank=True)
    litem_asset_url = models.URLField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.litem_name

    def __str__(self):
        return "{}__{}-{}".format(self.lesson, self.litem_seqnum, self.litem_name)