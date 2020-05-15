from django.conf.urls import url
from demo import views

urlpatterns = [
    url(r'test$', views.demo),
    url(r'do$', views.do)
]
