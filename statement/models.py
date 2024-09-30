from django.db import models

from system.models import Department, User, Teacher


# Create your models here.
class Statement(models.Model):
    id = models.BigAutoField(primary_key=True)
    # natural_year = models.CharField('自然年', max_length=4)
    academic_year = models.CharField('学年', max_length=4)
    # semester = models.CharField('学期', max_length=1)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name='教师ID')
    # teaching = models.FloatField('教学工作量', default=0.0)
    # practical = models.FloatField('实践工作量', default=0.0)
    total = models.FloatField('总工作量', default=0.0)
    creator = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='statement_creator',
                                verbose_name='创建者')
    updator = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='statement_updator',
                                verbose_name='更新者')
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = '工作量明细'
        verbose_name_plural = verbose_name

    def __str__(self) -> str:
        return self.teacher.name
