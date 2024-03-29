# Generated by Django 4.2 on 2023-05-23 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopsy', '0002_category_alter_signup_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pro_name', models.CharField(max_length=50, null=True)),
                ('pro_price', models.IntegerField(max_length=50, null=True)),
                ('pro_description', models.TextField(max_length=100, null=True)),
                ('pro_image', models.ImageField(null=True, upload_to='')),
                ('pro_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopsy.category')),
            ],
        ),
    ]
