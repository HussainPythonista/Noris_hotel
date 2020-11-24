from django.db import models

# Create your models here.
class AdminStuff(models.Model):
    type_room=models.CharField(max_length=20)
    image=models.ImageField(upload_to='pics')
    start_price=models.IntegerField(default=None)
    offer=models.BooleanField(default=False)
    def __str__(self):
        return f'{self.type_room} with staring from {self.start_price} dollars'
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