# Generated by Django 3.2.5 on 2021-07-24 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0009_alter_users_user_chores'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='user_chores',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='User.chores'),
        ),
    ]
