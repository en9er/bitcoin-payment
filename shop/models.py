from django.db import models
from account.models import CustomUser
from PIL import Image
from django.urls import reverse
import datetime


def get_product_url(obj, view_name):
    return reverse(view_name, kwargs={'ct_model': Card, 'slug': obj.slug})


class MinResolutionException(Exception):
    pass


class MaxResolutionException(Exception):
    pass


class LatestProductsManager:

    @staticmethod
    def get_products_for_main_page(*args, **kwargs):
        with_respect_to = kwargs.get('with_respect_to')
        products = []
        ct_model_products = Card.objects.all().order_by('-id')[:5]
        products.extend(ct_model_products)
        if with_respect_to:
            return sorted(products, key=lambda x: x.category.name.startswith(with_respect_to), reverse=True)
        return products


class LatestProducts:

    objects = LatestProductsManager()


class Category(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Card(models.Model):
    MIN_RESOLUTION = (300, 400)
    MAX_RESOLUTION = (2000, 3000)
    MAX_IMAGE_SIZE = 5242880
    image = models.ImageField()
    owner = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE, related_name='owner', null=True)
    creator = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE, related_name='creator', null=True)
    title = models.CharField(max_length=128)
    creation_time = models.DateTimeField(default=datetime.datetime.now())
    description = models.CharField(max_length=512)
    price = models.FloatField()
    favorite = models.PositiveIntegerField(default=0)
    views = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(to=Category, verbose_name="Category", on_delete=models.SET_DEFAULT, default=None, null=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    # def save(self, *args, **kwargs):
    #     image = self.image
    #     img = Image.open(image)
    #     if image.size > self.MAX_IMAGE_SIZE:
    #         raise MinResolutionException()
    #     if img.width < self.MIN_RESOLUTION[0] or img.height < self.MIN_RESOLUTION[1]:
    #         raise MinResolutionException(f"Image resolution {img.width}x{img.height} is less the required")
    #     if img.width > self.MAX_RESOLUTION[0] or img.height > self.MAX_RESOLUTION[1]:
    #         raise MaxResolutionException(f"Image resolution {img.width}x{img.height}  is bigger then the required")
    #     super().save(*args, **kwargs)

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')
