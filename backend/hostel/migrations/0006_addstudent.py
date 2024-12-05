# Generated by Django 5.1 on 2024-08-25 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0005_student_passportphoto'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roomNo', models.CharField(max_length=10)),
                ('bedNo', models.CharField(max_length=10)),
                ('std_pass', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('collageName', models.CharField(max_length=100)),
                ('phoneNo', models.CharField(max_length=15)),
                ('currentSem', models.IntegerField()),
                ('course', models.CharField(max_length=100)),
                ('hscPercentage', models.CharField(max_length=100)),
                ('studentType', models.CharField(max_length=100)),
                ('baseName', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
                ('taluko', models.CharField(max_length=100)),
                ('village', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('hscResult', models.FileField(upload_to='images/')),
                ('adharCard', models.FileField(upload_to='images/')),
                ('collageFeeRecipt', models.FileField(upload_to='images/')),
                ('passportPhoto', models.FileField(upload_to='images/')),
            ],
        ),
    ]
