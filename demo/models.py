from common.model import BaseModel
from django.db import models


class Book(BaseModel):
    name = models.CharField(verbose_name='书名', max_length=50, blank=True, null=True)
    author = models.CharField(verbose_name='作者', max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'book'
