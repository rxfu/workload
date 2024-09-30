from django.contrib import admin
from django.contrib.admin import display
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from statement.models import Statement
from system.models import Department


# Register your models here.
class StatementResource(resources.ModelResource):
    def __init__(self, **kwargs):
        super().__init__()
        self.user = kwargs['user']

    def before_import_row(self, row, **kwargs):
        department = Department.objects.get(name=row['单位'])

        row['academic_year'] = row['年度']
        row['department_id'] = department.id
        row['teacher_id'] = row['工号']
        row['total'] = row['工作量']

    def before_save_instance(self, instance, row, **kwargs):
        instance.creator = instance.updator = self.user

    class Meta:
        model = Statement
        fields = ('academic_year', 'semester', 'department', 'teacher', 'total')


@admin.register(Statement)
class StatementAdmin(ImportExportModelAdmin):
    resource_class = StatementResource
    list_display = ['tid', 'department', 'teacher_name', 'academic_year', 'total']
    list_filter = ['academic_year', 'teacher__department']
    ordering = ('teacher_id', 'academic_year')
    search_fields = ['teacher__id', 'teacher__name']

    @display(description='所属学院')
    def department(self, obj):
        return obj.teacher.department

    @display(description='工号')
    def tid(self, obj):
        return obj.teacher_id

    @display(description='教师姓名')
    def teacher_name(self, obj):
        return obj.teacher
