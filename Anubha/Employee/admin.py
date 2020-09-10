from django.contrib import admin
# Register your models here.
from .models import users, leave_application
admin.site.register(users)
admin.site.register(leave_application)
