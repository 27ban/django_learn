from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_learn.settings")
app = Celery(__name__)
app.config_from_object('django_learn.settings')
app.autodiscover_tasks(settings.INSTALLED_APPS)

