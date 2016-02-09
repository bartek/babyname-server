from django.conf.urls import url

from .views import (
    NameCollectionDetailView,
    NameCollectionRootView,
    NameList,
)

urlpatterns = [
    url(r'names/', NameList.as_view()),
    url(r'collections/', NameCollectionRootView.as_view()),
    url(r'collections/(?P<share_code>\w+)/$', NameCollectionDetailView.as_view())
]
