# Generated by Django 5.1.3 on 2024-11-26 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('due_date', models.DateField(blank=True, null=True)),
                ('status', models.CharField(choices=[('OPEN', 'Open'), ('WORKING', 'Working'), ('COMPLETED', 'Completed')], default='OPEN', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]