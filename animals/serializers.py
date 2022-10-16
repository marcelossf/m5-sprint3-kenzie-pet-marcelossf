from .models import Animal
from rest_framework import serializers
from .validator import ValidateCamps
from rest_framework.response import Response
from rest_framework.views import status
from traits.serializers import TraitSerializer
from groups.serializers import GroupSerializer
from .models import Animal

class AnimalSerializer(serializers.Serializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    name = serializers.CharField()
    age = serializers.IntegerField()
    weight = serializers.FloatField()
    sex = serializers.CharField()
    traits = TraitSerializer(many=True, read_only=True)
    group = GroupSerializer(read_only=True)
    # age_in_human_years = serializers.SerializerMethodField(read_only=True, method_name=Animal.convert_dog_age_to_human_years)

    def create(self, validated_data):
        newAnimal = Animal.objects.get_or_create(**validated_data)

        return newAnimal

    def update(self, instance, validated_data):
        # response = ValidateCamps.verify_camps(validated_data)

        # if(response.is_valid()):
        #     return Response({"{response.field}": "You can not update {response.field} property."}, status.HTTP_422_UNPROCESSABLE_ENTITY)

        instance.name = validated_data.get('name', instance.name)
        instance.age = validated_data.get('age', instance.age)
        instance.weight = validated_data.get('weight', instance.weight)
        instance.save()
        return instance