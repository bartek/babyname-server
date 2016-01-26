from rest_framework import generics

from .models import Name, NameCollection
from .serializers import (
    NameCollectionSerializer,
    NameSerializer,
)


class NameList(generics.ListAPIView):
    queryset = Name.objects.all()
    serializer_class = NameSerializer


class ShareCodeView(generics.RetrieveUpdateDestroyAPIView):
    """
    Fetch, update, or delete NameCollection instances.
    """
    queryset = NameCollection.objects.all()
    serializer_class = NameCollectionSerializer
    lookup_field = 'share_code'
