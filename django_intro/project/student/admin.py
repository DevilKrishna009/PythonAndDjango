from django.contrib import admin
from student.models import StudentDetailModel, StudentEducationModel
# Register your models here.

admin.site.register(StudentDetailModel)
admin.site.register(StudentEducationModel)