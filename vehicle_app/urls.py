from django.conf.urls import url
from .views import get_last_points

urlpatterns = [
    url('^last_points/$', get_last_points, name='last_points')
]
