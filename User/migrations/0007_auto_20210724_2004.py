# Generated by Django 3.2.5 on 2021-07-24 17:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0006_remove_users_user_chores'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='user_chores',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='User.chores'),
        ),
        migrations.AlterField(
            model_name='chores',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='chores',
            name='name',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
