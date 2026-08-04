from django.contrib import admin
from . models import *
# Register your models here.
admin.site.register(Visit)
admin.site.register(Prescription)
admin.site.register(PrescriptionItem)




#             python manage.py runserver