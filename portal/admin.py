from django.contrib import admin
from portal.models import User
from .models import *
# Register your models here.
admin.site.register(User)
admin.site.register(Document)
admin.site.register(student)