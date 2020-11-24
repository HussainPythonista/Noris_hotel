from django.db import models

# Create your models here.
class Room(models.Model):
    ROOM_CATEGORY = [
        ('Dlx','Delux'),
        ('Lux','Luxurious'),
        ('Ete','elite'),
    ]
    number=models.IntegerField()
    caregory=models.CharField(max_length=3,choices=ROOM_CATEGORY)
    beds=models.IntegerField()
    capacity=models.IntegerField()
    def __str__(self):
        return f'{self.number}.{self.caregory} with {self.beds} for {self.capacity} people'