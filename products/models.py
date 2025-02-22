from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=20)
    description = models.TextField()
    months_used = models.IntegerField()
    image = models.ImageField(upload_to='products/',null=True)
    created_at = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return self.name
