from django.contrib import admin
from .models import *

# Register your models here.
class CourseModelAdmin(admin.ModelAdmin):
    list_display = ["_Title","TimeStamp"]
    class Meta:
        model = Course

admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Lessons_item)