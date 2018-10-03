import random
import os
from django.db import models

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext



def upload_image_path(isinstance, filename):
    print(isinstance)
    print(filename)
    new_filename = random.randint(1,651899816351684)
    name, ext = get_filename_ext(filename)
    final_filname = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "products/{new_filename}/{final_filename}".format(new_filename=new_filename, final_filname=final_filname)

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(max_digits=20, decimal_places=2, default=39.99)
    image = models.ImageField(upload_to='products/', null=True, blank=True)

    def __str__(self):
        return self.title
    