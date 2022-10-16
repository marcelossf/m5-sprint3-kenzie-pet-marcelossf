from django.test import TestCase
from animals.models import Animal

class AnimalTestCase(TestCase):
    @classmethod
    def setUpTestData(self):
        Animal.objects.create(name="lion", age=6, weight=30, sex="Macho", group={"name": "cão", "scientific_name": "canis familiaris"})
        Animal.objects.create(name="cat", age=6, weight=30, sex="Femea", group={"name": "gato", "scientific_name": "gatis familiaris"})

    
