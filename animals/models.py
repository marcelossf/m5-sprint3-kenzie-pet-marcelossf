from django.db import models
import math

class SexChoice(models.TextChoices):
    MACHO = 'Macho',
    FEMEA = 'Fêmea',
    NAO_INFORMADO = 'Não informado'

class Animal(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    weight = models.FloatField()
    sex = models.CharField(
        max_length=15, 
        choices = SexChoice.choices,
        default = SexChoice.NAO_INFORMADO
    )

    traits = models.ManyToManyField('traits.Trait', related_name='animals')

    group = models.ForeignKey(
        'groups.Group', on_delete=models.CASCADE, related_name='animal'
    )

    def convert_dog_age_to_human_years(self):
        human_age = int(16 * math.log(self.age) + 31)
        return human_age 