from django.db import models

# Create your models here.
class registration(models.Model):
    name=models.CharField(max_length=100)
    phone=models.PositiveBigIntegerField(default=+91)
    email=models.EmailField(default="gmail.com")
    linkedin=models.TextField(default="www.linkedin.com")
    graduation_year=models.PositiveIntegerField(default=2030)

