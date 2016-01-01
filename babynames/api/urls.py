from django.conf.urls import url

from .views import NameList

urlpatterns = [
    url(r'names/', NameList.as_view())
]
