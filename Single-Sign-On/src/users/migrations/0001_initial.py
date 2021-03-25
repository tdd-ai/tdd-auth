# Generated by Django 3.1.7 on 2021-03-25 16:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import users.managers
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('joining_date', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='static')),
                ('first_name', models.CharField(max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='last name')),
                ('nickname', models.CharField(blank=True, max_length=30, null=True, verbose_name='nickname')),
                ('affiliation', models.CharField(blank=True, max_length=64, null=True, verbose_name='affiliation')),
                ('is_active', models.BooleanField(default=True, verbose_name='is active')),
                ('is_staff', models.BooleanField(default=False, verbose_name='staff')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('admin_org', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='admin', to='users.organization')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('organization', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='users', to='users.organization')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', users.managers.CustomUserManager()),
            ],
        ),
        migrations.CreateModel(
            name='OrganizationJoinRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='join_requests', to='users.organization')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='org_requests', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('org', 'user')},
            },
        ),
    ]
