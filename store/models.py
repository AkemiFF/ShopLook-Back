from django.db import models

# pour test uniquement


class Product(models.Model):

    product_name = models.CharField(max_length=45)
    slug = models.SlugField(max_length=128)
    price = models.FloatField(default=0.0)
    stock = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    thumbnail = models.ImageField(upload_to="img", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Produit"
