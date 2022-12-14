from random import choices
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField('Nome', max_length=150)
    description = models.TextField('Descrição', blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']

    def __str__(self):
        return self.name


class Task(models.Model):
    
    PRIORITY_CHOICES = (
        ('B', 'Baixa'),
        ('M', 'Média'),
        ('A', 'Alta'),
    )

    STATUS_CHOICES = (
        ('EX', 'Em execução'),
        ('PD', 'Pendente'),
        ('CD', 'Concluida'),
    )
    
    name = models.CharField('tarefa', max_length=200)
    description = models.TextField('Descrição')
    end_date = models.DateField('Data final', auto_now=False, auto_now_add=False)
    priority = models.CharField('Prioridade', max_length=1, choices=PRIORITY_CHOICES)
    category = models.ManyToManyField(Category)
    status = models.CharField('Status', max_length=2, choices=STATUS_CHOICES)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Tarefa'
        verbose_name_plural = 'Tarefas'
        ordering = ['id']
    
    def __str__(self):
        return self.name

    def list_categories(self):
        return ", ".join([c.name for c in self.category.all()])
    list_categories.short_description = "Categorias"