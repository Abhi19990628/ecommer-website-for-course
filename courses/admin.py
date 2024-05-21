from django.contrib import admin

from courses.models import Course ,Learning, Prerequisite , Tag , Video


class Tagadmin(admin.TabularInline):
    model = Tag

class Learningadmin(admin.TabularInline):
    model = Learning
    
class Prerequisiteadmin(admin.TabularInline):
    model = Prerequisite
    
    
class CourseAdmin(admin.ModelAdmin):
    inlines=[Tagadmin,Learningadmin,Prerequisiteadmin]
    
admin.site.register(Course,CourseAdmin)
admin.site.register(Video)