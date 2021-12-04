# Generated by Django 3.2.8 on 2021-12-03 08:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0003_auto_20211203_0816'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='unique_id',
        ),
        migrations.RemoveField(
            model_name='subcategory',
            name='unique_id',
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_category', models.CharField(choices=[('101', 'Allergies'), ('102', 'Birth Control'), ('103', 'Common Cold'), ('104', 'Chronic Pain'), ('105', 'Digestive Health'), ('106', 'Eczema'), ('107', 'Heart Disease'), ('108', 'Oral Health')], default='101', max_length=20)),
                ('name', models.CharField(max_length=255)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.ImageField(upload_to='images')),
                ('url', models.URLField(max_length=255)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.category')),
            ],
        ),
    ]
