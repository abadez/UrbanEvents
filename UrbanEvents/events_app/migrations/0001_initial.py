from django.conf import settings
from django.contrib.gis.db import models
from django.db import migrations
import django.db.models.deletion
from django.contrib.auth.models import User
from django.contrib.postgres.operations import CreateExtension

def forwards_func(apps, schema_editor):
    # Create a superuser
    User.objects.create_superuser(username='admin', email='admin@events_app.com', password='admin')
    # Create users
    User.objects.create_user(username='user', email='user@events_app.com', password='user')
    User.objects.create_user(username='user2', email='user2@event_app.com', password='user2')


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        # Add postgis extension
        CreateExtension('postgis'),

        # Create table
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=150)),
                ('geo_location', models.PointField()),
                ('creation_date', models.DateTimeField()),
                ('modify_date', models.DateTimeField(null=True)),
                ('state', models.IntegerField(default=0)),
                ('category', models.IntegerField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),

        # Populate table with initial data
        migrations.RunPython(forwards_func),
    ]
