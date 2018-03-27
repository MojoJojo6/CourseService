from django.db import models


class Category(models.Model):
    """
    Category of Courses
    """
    category_name   = models.CharField(max_length=50)
    date_created    = models.DateTimeField(auto_now_add=True)
    date_modified   = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category_name


class Course(models.Model):
    """
    Course table for course service
    """
    my_category         = models.ForeignKey(Category, related_name='courses', on_delete=models.PROTECT)
    course_name         = models.CharField(max_length=50)
    course_description  = models.CharField(max_length=200)
    faculty_id          = models.BigIntegerField()  # uid of Faculty
    date_created        = models.DateTimeField(auto_now_add=True)
    date_modified       = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.course_name

    def __str__(self):
        return self.course_name


class Lesson(models.Model):
    """
    Lesson in Course model
    """
    my_course           = models.ForeignKey(Course, related_name='lessons', on_delete=models.CASCADE)
    lesson_name         = models.CharField(max_length=50)
    lesson_seqname      = models.IntegerField()
    lesson_description  = models.CharField(max_length=200)
    date_created        = models.DateTimeField(auto_now_add=True)
    date_modified       = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.lesson_name

    def __str__(self):
        return self.lesson_name


class Lessons_item(models.Model):
    """
    Lesson item model
    """
    my_course               = models.ForeignKey(Course, on_delete=models.CASCADE)
    my_lesson               = models.ForeignKey(Lesson, related_name='lesson_items', on_delete=models.CASCADE)
    lesson_item_name        = models.CharField(max_length=50)
    lesson_item_seqname     = models.IntegerField()
    lesson_item_asset_link  = models.CharField(max_length=200, null=True, blank=True)
    lesson_item_description = models.CharField(max_length=200)
    date_created            = models.DateTimeField(auto_now_add=True)
    date_modified           = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.lesson_item_name

    def __str__(self):
        return self.lesson_item_name
