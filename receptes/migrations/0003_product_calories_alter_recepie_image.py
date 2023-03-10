# Generated by Django 4.1.5 on 2023-01-12 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receptes', '0002_alter_recepie_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='calories',
            field=models.PositiveSmallIntegerField(default=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recepie',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='receptes/images'),
        ),
    ]
