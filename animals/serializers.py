from .models import Animal
from rest_framework import serializers
from traits.serializers import TraitSerializer
from groups.serializers import GroupSerializer

class AnimalSerializer(serializers.Serializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    name = serializers.CharField()
    age = serializers.IntegerField()
    weight = serializers.FloatField()
    sex = serializers.CharField()
    traits = TraitSerializer(many=True, read_only=True)
    group = GroupSerializer(read_only=True)
    age_in_human_years = serializers.SerializerMethodField()

    def get_age_in_human_years(self, obj):        
        return obj.convert_dog_age_to_human_years()

    def create(self, validated_data):
        newAnimal = Animal.objects.get_or_create(**validated_data)

        return newAnimal

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.age = validated_data.get('age', instance.age)
        instance.weight = validated_data.get('weight', instance.weight)
        instance.save()
        return instance