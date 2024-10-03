# Generated by Django 5.0.3 on 2024-03-24 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='status',
            field=models.CharField(choices=[('P', 'Pending'), ('A', 'Accepted'), ('B', 'Borrowed'), ('N', 'Null')], default='N', max_length=1),
        ),
    ]
