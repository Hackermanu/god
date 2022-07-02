from django.db import models
class Bike(models.Model):
    bike_name=models.CharField(max_length=50)
    bike_company=models.CharField(max_length=50)
    bike_milage=models.IntegerField(default=True)
    bike_price=models.BigIntegerField(default=True)

    def __str__(self):
        return self.bike_name