# Generated by Django 5.1.3 on 2024-12-02 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.CharField(max_length=2)),
                ('father_name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'student_table',
            },
        ),
    ]