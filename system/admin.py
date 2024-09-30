from django.contrib import admin
from django.contrib.admin import display

from system.models import User, Department, Teacher


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'name', 'email', 'department', 'is_staff', 'is_active', 'last_login']
    list_filter = ['department']
    search_fields = ['username']

    @display(description='姓名')
    def name(self, obj):
        return obj.last_name + obj.first_name


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'department']
    list_filter = ['department']
    ordering = ('id',)
    search_fields = ['id', 'name']


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    ordering = ('id',)
