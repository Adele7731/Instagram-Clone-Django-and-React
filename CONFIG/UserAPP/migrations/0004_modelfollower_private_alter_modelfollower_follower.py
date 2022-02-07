# Generated by Django 4.0.2 on 2022-02-07 22:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UserAPP', '0003_alter_modelfollower_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelfollower',
            name='private',
            field=models.BooleanField(default=False, verbose_name='Gizli Hesap mı'),
        ),
        migrations.AlterField(
            model_name='modelfollower',
            name='follower',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followers', to=settings.AUTH_USER_MODEL, verbose_name='Takip edilen'),
        ),
    ]