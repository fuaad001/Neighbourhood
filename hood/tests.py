from django.test import TestCase
from .models import *
import datetime as dt

class NeighbourhoodTestClass(TestCase):
    def setUp(self):
        self.user = User(id = 5, username = 'photolee', password = 'Qwerty123', email = 'photolee@gmail.com')
        self.Neighbourhood = Neighbourhood(id = 5, name = 'fuaadVille', admin = self.user, location = 'moringa')

    def tearDown(self):
        Neighbourhood.objects.all().delete()
        User.objects.all().delete()
