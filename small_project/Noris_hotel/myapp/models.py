from django.db import models

# Create your models here.
class AdminStuff(models.Model):
    type_room=models.CharField(max_length=20)
    image=models.ImageField(upload_to='pics')
    start_price=models.IntegerField(default=None)