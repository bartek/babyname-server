from django.conf.urls import url

from .views import (
    NameList,
    ShareCodeView,
)

urlpatterns = [
    url(r'names/', NameList.as_view()),
    url(r'share_codes/(?P<share_code>\w+)/$', ShareCodeView.as_view())
]
