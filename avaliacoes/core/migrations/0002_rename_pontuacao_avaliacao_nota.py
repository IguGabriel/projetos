# Generated by Django 5.0.6 on 2024-06-10 21:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='avaliacao',
            old_name='pontuacao',
            new_name='nota',
        ),
    ]
