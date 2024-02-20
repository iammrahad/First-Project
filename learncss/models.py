from django.db import models

class Css(models.Model):
    title = models.CharField(max_length=50)
    