from django.test import TestCase

from .constants import NEUTRAL
from .models import NameCollection, Name, names_difference_with_share_code


class NameCollectionTest(TestCase):
    def test_names_difference_with_share_code(self):
        """
        Should return a subset of names based on inputted favourites/ignored.
        """
        NameCollection.objects.create(
            share_code='foo',
            favourites=[1, 6, 9],
            ignored=[3],
        )

        for i in [1, 6, 9, 3, 4]:
            Name.objects.create(
                id=i,
                name='Foo {}'.format(i),
                gender=NEUTRAL,
            )

        difference = names_difference_with_share_code(
            Name.objects.all(),
            'foo',
        )

        # There is no ignored/favourited id of 4
        self.assertEqual(list(difference.values_list('id', flat=True)), [4])
