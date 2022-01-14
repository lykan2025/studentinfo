from django.contrib import admin
from .models import StudentInfo,StudentAcademics
# Register your models here.

class StudentInfoAdmin(admin.ModelAdmin):
    list_display=('Roll_no','Name','Class','School','Mobile','Address')

class StudentAcademicsAdmin(admin.ModelAdmin):
    list_display=('Roll_no','Maths','Physics','Chemistry','Biology','English')


admin.site.register(StudentInfo,StudentInfoAdmin)
admin.site.register(StudentAcademics,StudentAcademicsAdmin)