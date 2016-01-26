from rest_framework import serializers

from .models import Name, NameCollection


class NameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Name
        fields = ('id', 'name', 'gender')


class NameCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = NameCollection
        fields = (
            'share_code', 'preferred_gender',
            'favourites', 'ignored',
        )
