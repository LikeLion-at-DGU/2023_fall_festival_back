# Generated by Django 4.2.5 on 2023-10-07 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_alter_chat_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='icon',
            field=models.CharField(choices=[('cry', 'cry'), ('hip', 'hip'), ('festival', 'festival'), ('fire', 'fire'), ('heart', 'heart'), ('haapy', 'haapy'), ('best', 'best')], default='cry', max_length=10),
        ),
    ]
