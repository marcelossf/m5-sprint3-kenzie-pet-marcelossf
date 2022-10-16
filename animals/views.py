from .validator import AnimalValidator

from rest_framework.views import APIView, status
from rest_framework.response import Response

from .models import Animal
from .serializers import AnimalSerializer
from groups.serializers import GroupSerializer
from groups.models import Group
from traits.models import Trait

class AnimalView(APIView):
    def get(self, request):
        animals = Animal.objects.all()
        animals_dict = []
        [animals_dict.append(AnimalSerializer(animal).data) for animal in animals]
        
        return Response(animals_dict)

class AnimalCreateView(APIView):
    def post(self, request):
            validator = AnimalValidator(**request.data)
            valid_data = validator.is_valid()
            if not valid_data:
                return Response(validator.errors, status.HTTP_400_BAD_REQUEST)

            group_data = request.data['group']
            trait_data = request.data['traits']

            animal_data = {'name':request.data['name'], 'age':request.data['age'], 'weight':request.data['weight'], 'sex':request.data['sex']}

            group_serializer = GroupSerializer(data=group_data)
            
            serializer = AnimalSerializer(data=animal_data)

            if serializer.is_valid() and group_serializer.is_valid():
                
                g1 = Group.objects.get_or_create(**group_data)

                a1 = Animal.objects.create(**animal_data, group=g1[0])
                
                for trait in trait_data:
                    a1.traits.add(Trait.objects.get_or_create(**trait)[0])
                return Response(AnimalSerializer(a1).data, status.HTTP_201_CREATED)
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    
class AnimalUpdateView(APIView):
    def patch(self, request, animal_id):
        try:
            validator = AnimalValidator(**request.data)
            valid_data = validator.valid_update(data_request=request.data)

            if not valid_data:
                return Response(validator.errors, status.HTTP_400_BAD_REQUEST)

            animal = Animal.objects.get(id=animal_id)
            serializer = AnimalSerializer(animal, request.data, partial=True)
            valid_data = serializer.is_valid()
            if valid_data:
                serializer.save()
                
                return Response(serializer.data)

        except Animal.DoesNotExist:
            return Response({'detail': 'Not found'}, status.HTTP_404_NOT_FOUND)

class AnimalViewByID(APIView):
    def get(self, request, animal_id):
        try:
            animal = Animal.objects.get(id=animal_id)
            serializer = AnimalSerializer(animal)                
            return Response(serializer.data)

        except Animal.DoesNotExist:
            return Response({'detail': 'Not found'}, status.HTTP_404_NOT_FOUND)

class AnimalDeleteView(APIView):
    def delete(self, request, animal_id):
        try:
            animal = Animal.objects.get(id=animal_id)
            animal.delete()

            return Response({})
        except Animal.DoesNotExist:
            return Response({'detail': 'Not found'}, status.HTTP_404_NOT_FOUND)
