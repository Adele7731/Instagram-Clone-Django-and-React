# Generated by Django 4.0.2 on 2022-02-07 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PostAPP', '0003_remove_modelpost_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelpost',
            name='images',
            field=models.FileField(default='', upload_to='Posts'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='ModelPostImages',
        ),
    ]
