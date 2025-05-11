from django.db import models

# Create your models here.
class Item_List(models.Model):
    Category_name = models.CharField(max_length=15)
    def __str__(self):
        return self.Category_name
class Items(models.Model):
    Item_name = models.CharField(max_length=15)
    description = models.TextField(blank=False)
    Price = models.IntegerField()
    Category = models.ForeignKey(Item_List, related_name='Name', on_delete=models.CASCADE)
    Image = models.ImageField(upload_to='Items/')

    def __str__(self):
        return self.Item_name
class AboutUs(models.Model):
    Description = models.TextField(blank=False)
    
class Feedback(models.Model):
    Name = models.CharField(max_length=15)
    Description = models.TextField(blank=False)
    Rating = models.IntegerField()
    Image = models.ImageField(upload_to='Items/', blank=True)

    def __str__(self):
        return self.Name

class Booktable(models.Model):
    Name = models.CharField(max_length=15)
    Phone_Number = models.IntegerField()
    Email = models.EmailField()
    total_person = models.IntegerField()
    booking_date = models.DateField()

    def __str__(self):
        return self.Name