from django.db import models
from PIL import Image



class Property(models.Model):
    property_type = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    landlord = models.CharField(max_length=255)
    neighbourhood = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=10)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    image = models.ImageField(upload_to='static/images/')

    def save(self, *args, **kwargs):
        super(Property, self).save(*args, **kwargs)
        img = Image.open(self.image.path)

        if img.height < 462 or img.width < 340:
            output_size = (462, 340)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def __str__(self):
        return self.address

# Create your models here.

