from django.db import models

# Create your models here.

    
class MenuModel(models.Model):
    Title = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=10,decimal_places=2)
    Inventory = models.IntegerField()
    
    def get_item(self):
        return f'{self.title} : {self.Price}'
    
class BookingModel(models.Model):
    Name = models.CharField(max_length=255)
    No_of_guests = models.IntegerField()
    BookingDate = models.DateTimeField(editable=True)
    
    