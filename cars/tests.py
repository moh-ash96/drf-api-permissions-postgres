from django.test import TestCase
from django.contrib.auth.models import User

from .models import Car
# Create your tests here.

class BigTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = User.objects.create_user(username="mohammad", password="1234")
        testuser1.save()

        test_car = Car.objects.create(
            admin=testuser1, name = "lancer", maker = "mitsubishi", year = "2010",
        )
        test_car.save()
    
    def test_vehicle_content(self):
        car = Car.objects.get(id=1)
        expected_admin = f"{car.admin}"
        expected_name = f"{car.name}"
        expected_maker = f"{car.maker}"
        expected_year = f"{car.year}"
        self.assertEqual(expected_admin, "mohammad")
        self.assertEqual(expected_name, "lancer")
        self.assertEqual(expected_maker, "mitsubishi")
        self.assertEqual(expected_year, "2010")


