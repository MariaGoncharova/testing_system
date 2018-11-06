from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^tests$', views.tests, name='tests'),
#    url(r'^test/(\d+)$', views.test, name='test'),
]