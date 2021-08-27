from django.db import models

# Create your models here.
class Image(models.Model):
    photo = models.ImageField(upload_to="myimage/WhatsApp_Image_2021-06-22_at_6.14.18_PM_1.jpeg")
    date = models.DateTimeField(auto_now_add=True)