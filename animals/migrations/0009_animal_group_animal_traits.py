# Generated by Django 4.1.2 on 2022-10-15 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0004_remove_group_animals_alter_group_name_and_more'),
        ('traits', '0004_alter_trait_name'),
        ('animals', '0008_remove_animal_group_remove_animal_traits'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='group',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='animal', to='groups.group'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='animal',
            name='traits',
            field=models.ManyToManyField(related_name='animals', to='traits.trait'),
        ),
    ]