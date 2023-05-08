# Generated by Django 4.0.3 on 2023-05-04 00:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donneur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(blank=True, default='فاعل خير', max_length=50, null=True, verbose_name='الاسم')),
                ('tel', models.IntegerField(verbose_name='الهاتف')),
                ('password', models.CharField(max_length=10, verbose_name='كلمةالسر')),
                ('groupeSanguin', models.CharField(blank=True, choices=[('لا اعرف', 'لا اعرف'), ('O-', 'O-'), ('O+', 'O+'), ('A-', 'A-'), ('B-', 'B-'), ('AB-', 'AB-'), ('B+', 'B+'), ('AB+', 'AB+'), ('A+', 'A+')], max_length=10, null=True, verbose_name='زمرةالدم')),
                ('date_Dernier_Don', models.DateField(blank=True, null=True, verbose_name='تاريخ اخر تبرع')),
                ('wilaya', models.CharField(blank=True, choices=[(' الحوض الشرقي', 'الحوض الشرقي'), ('الحوض الغربي', 'الحوض الغربي'), ('لعصابة', 'لعصابة'), ('كوركول', 'كوركول'), ('لبراكنة', 'لبراكنة'), ('ترارزة', 'ترارزة'), ('أدرار', 'أدرار'), ('انواذيبو', 'انواذيبو'), ('تكانت', 'تكانت'), ('كيديماغا', 'كيديماغا'), ('تيرس زمور', 'تيرس زمور'), ('إنشيري', 'إنشيري'), ('انواكشوط', 'انواكشوط')], max_length=30, null=True, verbose_name='الولاية')),
            ],
            options={
                'verbose_name': 'متبرع',
                'verbose_name_plural': 'المتبرعون',
            },
        ),
        migrations.CreateModel(
            name='Hopital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=20, verbose_name='الاسم')),
                ('password', models.CharField(max_length=10, verbose_name='كلمة السر')),
            ],
            options={
                'verbose_name': 'مستشفى',
                'verbose_name_plural': 'المستشفيات',
            },
        ),
        migrations.CreateModel(
            name='Rendez_vous',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='التاريخ')),
                ('time', models.TimeField(verbose_name='الوقت')),
                ('lieu', models.CharField(max_length=15, verbose_name='المكان')),
                ('donneur_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.donneur', verbose_name='المتبرع')),
            ],
            options={
                'verbose_name': 'ميعاد',
                'verbose_name_plural': 'المواعيد',
            },
        ),
    ]
