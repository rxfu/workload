from django.contrib.auth.models import AbstractUser, Group
from django.db import models


# Create your models here.
class Department(models.Model):
    id = models.BigAutoField('单位ID', primary_key=True)
    name = models.CharField('名称', max_length=50)

    class Meta:
        verbose_name = '单位'
        verbose_name_plural = verbose_name

    def __str__(self) -> str:
        return self.name


class Teacher(models.Model):
    id = models.CharField('工号', max_length=8, primary_key=True)
    name = models.CharField('姓名', max_length=50)
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING, verbose_name='所属单位')

    class Meta:
        verbose_name = '教师'
        verbose_name_plural = verbose_name

    def __str__(self) -> str:
        return self.name


class User(AbstractUser):
    id = models.BigAutoField('用户ID', primary_key=True)
    department = models.ForeignKey(Department, null=True, blank=True, on_delete=models.DO_NOTHING,
                                   verbose_name='所属单位')

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self) -> str:
        return self.last_name + self.first_name
