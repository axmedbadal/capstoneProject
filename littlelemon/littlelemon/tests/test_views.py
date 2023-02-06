from django.test import TestCase
from restaurant.models import Menu
from django.urls import reverse
from restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):
    def setUp(self):
        self.lasagna = Menu.objects.create(
            title='Lasagna', price=8.00, inventory=100)
        self.salad = Menu.objects.create(
            title='Salad', price=5.00, inventory=100)

    def test_get_all(self):
        items = Menu.objects.all()
        serialized = MenuSerializer(items, many=True)
        # print(str(serialized.data))
        self.assertEqual(str(
            serialized.data), "[OrderedDict([('id', 1), ('title', 'Lasagna'), ('price', '8.00'), ('inventory', 100)]), OrderedDict([('id', 2), ('title', 'Salad'), ('price', '5.00'), ('inventory', 100)])]")

    def test_url_exist_at_location(self):
        response = self.client.get('/restaurant/menu/')
        self.assertEqual(response.status_code, 200)
