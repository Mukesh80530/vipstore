# Generated by Django 3.2.8 on 2021-12-03 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_auto_20211203_0812'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='sub_category',
        ),
        migrations.AddField(
            model_name='subcategory',
            name='sub_category',
            field=models.CharField(choices=[('101', 'Allergies'), ('102', 'Birth Control'), ('103', 'Common Cold'), ('104', 'Chronic Pain'), ('105', 'Digestive Health'), ('106', 'Eczema'), ('107', 'Heart Disease'), ('108', 'Oral Health')], default='101', max_length=20),
        ),
    ]
