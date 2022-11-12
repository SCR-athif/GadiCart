from django.db import models
import datetime

#Choice
YEAR_CHOICES = [(r, r) for r in range(1984, datetime.date.today().year + 1)]
Fuel_type = (
    ("Petrol","Petrol"),
    ("Diesel","Diesel"),
    ("CNG","CNG"),
    ("EV","EV"),
)

Vehicle_Type = (
    ("Bicycle","Bicycle"),
    ("JCB","JCB"),
    ("AutoRicksha","AutoRicksha"),
    ("BUS","BUS"),
    ("Lory","Lory"),
    ("Pickup","Pickup"),
)

Issues = (
    ("My item was sold(mention item id in detail section)","My item was sold(mention item id in decription)"),
    ("Report an abuse","Report an abuse"),
    ("Report fraud activity","Report fraud activity"),
    ("Secutrity Vulnerability","Secutrity Vulnerability",),
    ("other","other"),

)

Ownerships = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
    ("6", "6"),
    ("7", "7"),
    ("8", "8"),
)
#create
class Bike(models.Model):
    ID = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=20000, blank=True)
    Date = models.DateTimeField(auto_now_add=True)
    Price = models.IntegerField()
    Brand = models.CharField(max_length=200)
    year = models.IntegerField(choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    KM = models.IntegerField()
    Fuel = models.CharField(max_length=40, choices=Fuel_type, default='Petrol')
    Ownership = models.CharField(max_length=20,choices=Ownerships,default='1')
    Phone = models.CharField(max_length=12)
    Email = models.EmailField(max_length=120)
    Description =models.TextField()
    Image = models.ImageField(upload_to='images')


class Car(models.Model):
    ID = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=20000, blank=True)
    Date = models.DateTimeField(auto_now_add=True)
    Price = models.IntegerField()
    Brand = models.CharField(max_length=200)
    year = models.IntegerField(choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    KM = models.IntegerField()
    Fuel = models.CharField(max_length=40, choices=Fuel_type, default='Petrol')
    Ownership = models.CharField(max_length=20,choices=Ownerships,default='1')
    Phone = models.CharField(max_length=12)
    Email = models.EmailField(max_length=120)
    Description =models.TextField()
    Image = models.ImageField(upload_to='images')

class Other(models.Model):
    ID = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=20000, blank=True)
    Date = models.DateTimeField(auto_now_add=True)
    Price = models.IntegerField()
    Vehicle_Type = models.CharField(max_length=2000, choices=Vehicle_Type,default='bicycle')
    Brand = models.CharField(max_length=200)
    year = models.IntegerField(choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    KM = models.IntegerField()
    Fuel = models.CharField(max_length=40, choices=Fuel_type, default='Petrol')
    Ownership = models.CharField(max_length=20,choices=Ownerships,default='1')
    Phone = models.CharField(max_length=12)
    Email = models.EmailField(max_length=120)
    Description =models.TextField()
    Image = models.ImageField(upload_to='images')

class Reports(models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=200)
    Email = models.EmailField(max_length=200)
    Issue = models.CharField(max_length=500,choices=Issues,default='My item was sold(mention item id in decription)')
    Details = models.TextField()
