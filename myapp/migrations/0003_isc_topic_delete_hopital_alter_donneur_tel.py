# Generated by Django 4.0.3 on 2023-05-26 23:40

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_donneur_tel'),
    ]

    operations = [
        migrations.CreateModel(
            name='ISC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=20, verbose_name='الاسم')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='الهاتف')),
                ('email', models.EmailField(max_length=254, verbose_name='الايميل')),
                ('password', models.CharField(max_length=50, verbose_name='كلمة السر')),
                ('description', models.TextField(verbose_name='الوصف')),
            ],
            options={
                'verbose_name': 'مؤسسة صحية و خيرية ',
                'verbose_name_plural': '  مؤسسات صحية و خيرية ',
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=50, verbose_name='الموضوع')),
                ('contenu', models.TextField(max_length=300, verbose_name='المضمون')),
                ('created_dt', models.DateTimeField(auto_now_add=True, verbose_name='تاريخ النشر')),
                ('publier_de', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topics', to='myapp.isc', verbose_name='بواسطة')),
            ],
            options={
                'verbose_name': 'منشور',
                'verbose_name_plural': ' منشورات',
            },
        ),
        migrations.DeleteModel(
            name='Hopital',
        ),
        migrations.AlterField(
            model_name='donneur',
            name='tel',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='الهاتف'),
        ),
    ]
