from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100)
	
    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")
	
    def __str__(self):
        return self.name

class TodoList(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    content = models.TextField(blank=True)
    created = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
	
    class Meta:
        ordering = ["-created"]
		
    def __str__(self):
        return self.title