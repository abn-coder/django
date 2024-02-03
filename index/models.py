from django.db import models

# Create your models here.

class Social(models.Model):
    title = models.CharField(max_length=255, null=True)
    link = models.CharField(max_length=255, blank=True)
    icon = models.FileField(upload_to="uploads/social/")
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Соц. сети"
        verbose_name_plural = "Соц. сети"


class Nft(models.Model):
    title = models.CharField(max_length=255)
    image = models.FileField(upload_to="upload/nft/")
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    create_on = models.DateTimeField(auto_now=True)
    update_on = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

