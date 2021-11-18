# Generated by Django 3.1.7 on 2021-11-16 11:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name_plural': 'comment'},
        ),
        migrations.AlterModelOptions(
            name='comments',
            options={'verbose_name_plural': 'comments'},
        ),
        migrations.AlterModelOptions(
            name='editpages',
            options={'verbose_name_plural': 'editpages'},
        ),
        migrations.AlterModelOptions(
            name='joinus',
            options={'verbose_name_plural': 'joinus'},
        ),
        migrations.AlterModelOptions(
            name='photos',
            options={'verbose_name_plural': 'photos'},
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name_plural': 'profile'},
        ),
        migrations.AlterModelOptions(
            name='register',
            options={'verbose_name_plural': 'register'},
        ),
        migrations.AlterModelOptions(
            name='testimonials',
            options={'verbose_name_plural': 'testimonials'},
        ),
        migrations.AlterModelOptions(
            name='users',
            options={'verbose_name_plural': 'users'},
        ),
        migrations.AlterModelOptions(
            name='video',
            options={'verbose_name_plural': 'video'},
        ),
        migrations.AlterModelOptions(
            name='views',
            options={'verbose_name_plural': 'views'},
        ),
        migrations.AlterField(
            model_name='profile',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
