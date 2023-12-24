from django.db import models
from apps.users.models import User
from apps.common.models import TimeStampedModel


class Product(TimeStampedModel):
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('noactive', 'Not Active'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product,
        related_name='product_images',
        on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/', blank=True)

    def __str__(self):
        return f"{self.product.title} image"

    class Meta:
        verbose_name = "ProductImage"
        verbose_name_plural = "ProductImages"
