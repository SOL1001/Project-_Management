from django.contrib import admin
from .models import Employee, Account, ProjectUpload, Comment

admin.site.register(Employee)
admin.site.register(Account)
admin.site.register(ProjectUpload)
admin.site.register(Comment)