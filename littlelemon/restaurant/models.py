from django.db import models

class Menu(models.Model):
    title = models.CharField(max_length=200)  
    price = models.DecimalField(max_digits=10, decimal_places=2) 
    inventory = models.IntegerField()

    def __str__(self):
        return f'{self.title} : {str(self.price)}'
    
class Booking(models.Model):
    name = models.CharField(max_length=100)  
    no_of_guests = models.IntegerField() 
    booking_date = models.DateTimeField()

    def __str__(self):
        return f"{self.name} - {self.no_of_guests} guests"
    
# class MenuItem(models.Model):  
#                 title = models.CharField(max_length=255)  
#                 price = models.DecimalField(max_digits=6, decimal_places=2)  
#                 inventory = models.SmallIntegerField()  

#                 def __str__(self):
#                     return f'{self.title} : {self.price}'