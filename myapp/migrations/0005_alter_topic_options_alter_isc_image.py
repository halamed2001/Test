# Generated by Django 4.0.3 on 2023-05-27 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_isc_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='topic',
            options={'verbose_name': 'منشور', 'verbose_name_plural': ' المنشورات  '},
        ),
        migrations.AlterField(
            model_name='isc',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='photos/%y/%m/%d', verbose_name='صورة'),
        ),
    ]