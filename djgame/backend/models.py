from django.db import models

# Create your models here.
class producttable(models.Model):
    name=models.CharField(max_length=20)
    quntity=models.IntegerField()
    prize=models.IntegerField()
    image=models.ImageField(upload_to="product")

    def __str__(self):
        return self.name

    def formatted_price(self):
        return f"₹{self.prize}"