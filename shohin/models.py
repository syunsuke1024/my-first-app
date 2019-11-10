from django.db import models
from django.utils import timezone

class Shohin(models.Model):
    shohinmei=models.CharField(max_length=100)
    tenmei=models.CharField(max_length=50)
    kakaku=models.IntegerField(default=0)
    create_at=models.DateTimeField(default=timezone.now())

def __str__(self):
    return '<Shohin:id=' + str(self.id) + ', '+self.name + '(' + str(self.kakaku) + ') >'