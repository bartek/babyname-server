from rest_framework import generics

from .models import Name
from .serializers import NameSerializer


class NameList(generics.ListAPIView):
    queryset = Name.objects.all()
    serializer_class = NameSerializer
