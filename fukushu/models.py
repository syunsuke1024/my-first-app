from django.db import models
from django.utils.timezone import now

# Create your models here.
PRIORITY=(("success","AC"),("warning","MISS"),("danger","NOSUB"),("secondary","NOCHARENGE"),("dark","IMPOSSIBLE"),("link","NOTHING"))
class FukushuModel(models.Model):
    title = models.CharField(max_length=50,default='ABC〇〇〇')
    problem1 = models.CharField(
        max_length=50,
        choices=PRIORITY,
        default="secondary"

    )
    date1 = models.DateField(default=now())
    problem2 = models.CharField(
        max_length=50,
        choices=PRIORITY,
        default = "secondary"
    )
    date2 = models.DateField(default=now())
    problem3 = models.CharField(
        max_length=50,
        choices=PRIORITY,
        default="secondary"
    )
    date3 = models.DateField(default=now())
    problem4 = models.CharField(
        max_length=50,
        choices=PRIORITY,
        default="secondary"
    )
    date4 = models.DateField(default=now())
    def __str__(self):
        return self.title
