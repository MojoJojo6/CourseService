from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,BaseUserManager,
)


"""
    Litem points to a lesson, lesson points to a course, course points to a category.
    
    "many ------> one" relationships implemented by using foreign keys.
    
    On deletion of a lesson, all the associated litems will be deleted.
    On deletion of a category, course, all the associated courses and lessons respectively
    will not be deleted.
"""


class UserManager(BaseUserManager):

    def create_user(self, **validated_data):

        if not validated_data["email_id"]:
            raise ValueError("Email Id is required")
        if not validated_data["password"]:
            raise ValueError("Password is required")
        if not validated_data["first_name"]:
            raise ValueError("First Name is required")
        if not validated_data["last_name"]:
            raise ValueError("Last Name is required")
        if validated_data["role"] is None:
            raise ValueError("Role is required")

        user_obj = self.model( email_id=self.normalize_email(validated_data["email_id"]))
        user_obj.first_name = validated_data["first_name"]
        user_obj.last_name = validated_data["last_name"]
        user_obj.role = validated_data["role"]
        user_obj.mobile_number = validated_data["mobile_number"]
        user_obj.staff = validated_data["staff"]
        user_obj.admin = validated_data["admin"]
        user_obj.active = validated_data["active"]
        user_obj.set_password(validated_data["password"])
        user_obj.save(using=self.db)
        return user_obj
    
    def create_superuser(self, **validated_data):
        validated_data['staff'] = True
        validated_data['admin'] = True
        validated_data['active'] = True
        return self.create_user(**validated_data)

    def create_staffuser(self, **validated_data):
        validated_data['staff'] = True
        validated_data['admin'] = False
        validated_data['active'] = True
        return self.create_user(**validated_data)

    
class User(AbstractBaseUser):
    """ User Table for User Service"""
    roles = [(0, "Admin"), (1, "Faculty"), (2, "Student")]

    u_id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email_id = models.EmailField(max_length=255, unique=True)
    mobile_number = models.CharField(max_length=20)
    role = models.IntegerField(choices=roles)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email_id'
    REQUIRED_FIELDS = ['first_name','last_name','role', 'mobile_number']

    objects = UserManager()

    def get_full_name(self):
        return "{0} {1}".format(self.first_name,self.last_name)

    def get_short_name(self):
        return self.first_name

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    """String Function for All CharField in User Model"""
    def __str__(self):
        return self.email_id



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