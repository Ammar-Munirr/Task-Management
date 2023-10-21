from django.contrib import admin
from .models import Tasks,User



@admin.register(Tasks)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title','description','due_date','status','user']
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','username','first_name','last_name','email']