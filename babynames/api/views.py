from rest_framework import filters
from rest_framework import generics

from .models import (
    Name,
    NameCollection,
    names_difference_with_share_code,
)

from .serializers import (
    NameCollectionSerializer,
    NameSerializer,
)


class NameList(generics.ListAPIView):
    queryset = Name.objects.all()
    serializer_class = NameSerializer
    filter_backends = (filters.DjangoFilterBackend, )
    filter_fields = ('gender', )

    def get_queryset(self):
        """
        Optionally restrict the resulting names list

        If `with__share_code` is passed in the parameters, the resulting
        queryset will ensure to not return any names that have already been
        included in that NameCollection's data.
        """
        queryset = super(NameList, self).get_queryset()
        share_code = self.request.query_params.get('with__share_code', None)
        if share_code is None:
            return queryset

        # Fetch the subset of names.
        queryset = names_difference_with_share_code(queryset, share_code)

        return queryset


class ShareCodeView(generics.RetrieveUpdateDestroyAPIView):
    """
    Fetch, update, or delete NameCollection instances.
    """
    queryset = NameCollection.objects.all()
    serializer_class = NameCollectionSerializer
    lookup_field = 'share_code'
