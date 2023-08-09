from django.contrib.auth.models import AbstractUser
from store import baseModels


class Shopper(AbstractUser):
    def save(self, *args, **kwargs):

        baseModels.initialize_categories()
        super().save(*args, **kwargs)


# class Shopper(models.Model):
#     name = models.CharField(max_length=45, blank=False, default="")
#     email = models.CharField(max_length=45, null=True, blank=True)
#     phone_number = models.IntegerField(null=True, blank=True)
