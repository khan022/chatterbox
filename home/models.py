from django.db import models

# Create your models here.
class text_input(models.Model):
    textinput = models.CharField(max_length=160)