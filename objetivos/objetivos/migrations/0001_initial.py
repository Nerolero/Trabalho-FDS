# Generated by Django 5.1.7 on 2025-04-05 17:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Objetivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nome', models.CharField(max_length=1000)),
                ('Descrição', models.TextField()),
                ('Status', models.CharField(choices=[('pendente', 'Pendente'), ('ativa', 'Ativa'), ('completa', 'Completa')], default='pendente', max_length=20)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Objetivos', to='login.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Subtarefa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nome', models.CharField(max_length=255)),
                ('descrição', models.TextField()),
                ('Status', models.CharField(choices=[('pendente', 'Pendente'), ('ativa', 'Ativa'), ('completa', 'Completa')], default='pendente', max_length=20)),
                ('objetivo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Subtarefas', to='objetivos.objetivo')),
            ],
        ),
    ]
