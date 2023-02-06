from django.test import TestCase
from restaurant.models import Menu


class MenuTest(TestCase):
    def setUp(self):
        self.item = Menu.objects.create(
            title='Lasagna', price=7.75, inventory=100)

    def test_get_item(self):
        self.assertEqual(str(self.item), 'Lasagna : 7.75')

    def test_get_name(self):
        self.assertEqual(self.item.title, 'Lasagna')

    def test_get_price(self):
        self.assertEqual(self.item.price, 7.75)

    def test_get_inventory(self):
        self.assertEqual(self.item.inventory, 100)

    def test_instance(self):
        self.assertIsInstance(self.item, Menu)
