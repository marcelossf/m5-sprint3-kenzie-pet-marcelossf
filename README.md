# Kenzie Pet
# shell do Django
from animals.serializers import AnimalSerializer
from traits.serializers import TraitSerializer
from groups.serializers import GroupSerializer

from animals.models import Animal
from groups.models import Group
from traits.models import Trait


animal_data = {"name": "Beethoven", "age": 1, "weight": 30, "sex": "Macho"}
group_data = {"name": "cão", "scientific_name": "canis familiaris"}
trait_data = {"name": "peludo"}

# Validando e criando grupo
serializer = GroupSerializer(data=group_data)
serializer.is_valid()
# True
g1 = Group.objects.create(**serializer.validated_data)

# Validando e criando animal, já com grupo

serializer = AnimalSerializer(data=animal_data)
serializer.is_valid()
# True
a1 = Animal.objects.create(**serializer.validated_data, group=g1)

# Validando e criando trait, depois associando ao animal a1
serializer = TraitSerializer(data=trait_data)
serializer.is_valid()
# True

t1 = Trait.objects.create(**serializer.validated_data)
a1.traits.add(t1)