# Generated by Django 3.1.4 on 2020-12-28 19:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdashboardmodule',
            name='user',
            field=models.PositiveIntegerField(verbose_name='user', null=True)
        ),
        migrations.RunSQL("""
                    UPDATE dashboard_userdashboardmodule SET "user" = NULL 
                    WHERE NOT EXISTS ( SELECT id FROM auth_user WHERE id = dashboard_userdashboardmodule.user);
                    """
            
        ),
        migrations.AlterField(
            model_name='userdashboardmodule',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='user')
        ),
    ]
