from django.db import models
from django.utils.timezone import now
import datetime

status=(
('Dispatched', 'Dispatched'),
    ('Pending','Pending'),
    ('Complete','Complete'),
    ('Loaded','Loaded'),
    ('Unloaded','Unloaded')
)


class DriverModel(models.Model):
    name=models.CharField(max_length=100, unique=True)
    dl_no=models.CharField(max_length=100, unique=True)
    dl_expiry=models.DateField()
    finished_tasks=models.IntegerField(default=0)
    assigned_tasks=models.IntegerField(default=0)
    reputation=models.IntegerField(default=1)    
    def __unicode__(self):
        return self.name

class VehicleModel(models.Model):
    load_no=models.IntegerField( unique=True)
    model_no= models.IntegerField()
    vehicle_name= models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.vehicle_name

class OrderModel(models.Model):
    load=models.IntegerField()
    status=models.CharField(max_length=50, choices=status, default='Pending')
    customer=models.CharField(max_length=200)
    origin=models.CharField(max_length=100)
    destination=models.CharField(max_length=100)
    usd=models.IntegerField()
    ship_date=models.DateTimeField(default=now)
    del_date=models.DateTimeField(default='')
    vehicle_type=models.CharField(max_length=100)
    total_km=models.IntegerField()
    equipment_type=models.CharField(max_length=200)
    driver_name=models.ForeignKey(DriverModel, related_name='driver', to_field='dl_no')
    
    def __unicode__(self):
        return self.status
    

    
