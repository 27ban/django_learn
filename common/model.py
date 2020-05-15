from datetime import datetime
from django.db import models


class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    created_time = models.DateTimeField(verbose_name='创建日期', auto_now_add=True)
    updated_time = models.DateTimeField(verbose_name='更新日期', auto_now=True)

    class Meta:
        abstract = True
