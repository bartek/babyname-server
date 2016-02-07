from rest_framework import serializers

from .models import Name, NameCollection


class NameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Name
        fields = ('id', 'name', 'gender', 'popularity')


class NameCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = NameCollection
        fields = (
            'share_code', 'preferred_gender',
            'favourites', 'ignored',
        )
