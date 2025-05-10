from django.db import models

class CropProduct(models.Model):
    crop_name = models.CharField(max_length=100)
    market_price = models.DecimalField(max_digits=10, decimal_places=2)
    image_file = models.ImageField(upload_to='media/uploads/', blank=True, null=True)  
    location = models.CharField(max_length=100)
    harvest_days = models.IntegerField()
    harvest_date = models.DateField()
    contact_name = models.CharField(max_length=100)
    contact_phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.crop_name
