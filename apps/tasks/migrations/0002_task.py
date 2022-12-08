# Generated by Django 4.0.4 on 2022-04-24 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='tarefa')),
                ('description', models.TextField(verbose_name='Descrição')),
                ('end_date', models.DateField(verbose_name='Data final')),
                ('priority', models.CharField(choices=[('B', 'Baixa'), ('M', 'Média'), ('A', 'Alta')], max_length=1, verbose_name='Prioridade')),
                ('status', models.CharField(choices=[('EX', 'Em execução'), ('PD', 'Pendente'), ('CD', 'Concluida')], max_length=2, verbose_name='Status')),
                ('category', models.ManyToManyField(to='tasks.category')),
            ],
            options={
                'verbose_name': 'Tarefa',
                'verbose_name_plural': 'Tarefas',
                'ordering': ['id'],
            },
        ),
    ]
