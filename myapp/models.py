# Create your models here.
from django.db import models


# Create your models here.

class Restaurant(models.Model):
    restaurant_name = models.CharField(max_length=30)
    city_name = models.CharField(max_length=30)


    nos = models.DecimalField(decimal_places=0, max_digits=2)
    rem = models.DecimalField(decimal_places=0, max_digits=2)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.restaurant_name


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField()
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.email


class Book(models.Model):
    BOOKED = 'B'
    CANCELLED = 'C'

    TICKET_STATUSES = ((BOOKED, 'Booked'),
                       (CANCELLED, 'Cancelled'),)
    email = models.EmailField()
    name = models.CharField(max_length=30)
    userid =models.DecimalField(decimal_places=0, max_digits=2)
    restaurantid=models.DecimalField(decimal_places=0, max_digits=2)
    restaurant_name = models.CharField(max_length=30)
    city_name = models.CharField(max_length=30)


    nos = models.DecimalField(decimal_places=0, max_digits=2)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(choices=TICKET_STATUSES, default=BOOKED, max_length=2)

    def __str__(self):
        return self.email
class Mess(models.Model):
    mess_name = models.CharField(max_length=30)
    city_name = models.CharField(max_length=30)

    food_type=models.CharField(max_length=30)
    nos = models.DecimalField(decimal_places=0, max_digits=2)
    rem = models.DecimalField(decimal_places=0, max_digits=2)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    date = models.DateField()
    time = models.TimeField()
class Book1(models.Model):
    BOOKED = 'B'
    CANCELLED = 'C'

    TICKET_STATUSES = ((BOOKED, 'Booked'),
                       (CANCELLED, 'Cancelled'),)
    email = models.EmailField()
    name = models.CharField(max_length=30)
    userid = models.DecimalField(decimal_places=0, max_digits=2)
    messid = models.DecimalField(decimal_places=0, max_digits=2)
    mess_name = models.CharField(max_length=30)
    city_name = models.CharField(max_length=30)
    nos = models.DecimalField(decimal_places=0, max_digits=2)
    food_type = models.CharField(max_length=30)
    user_doc = models.FileField(null=True)




    price = models.DecimalField(decimal_places=2, max_digits=6)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(choices=TICKET_STATUSES, default=BOOKED, max_length=2)

    def __str__(self):
        return self.email





