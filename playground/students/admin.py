from django.contrib import admin
from students.models import StudentDetailModel, StudentContactDetailModel, StudentPrevEducationModel, \
    AddressDetailModel, PrevEducationModel

# Register your models here.

admin.site.register(StudentDetailModel)
admin.site.register(StudentContactDetailModel)
admin.site.register(StudentPrevEducationModel)
admin.site.register(AddressDetailModel)
admin.site.register(PrevEducationModel)
