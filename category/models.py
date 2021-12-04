from PIL import Image
from django.db import models

SUB_CATEGORY = (
    ("101", "Allergies"),
    ("102", "Birth Control"),
    ("103", "Common Cold"),
    ("104", "Chronic Pain"),
    ("105", "Digestive Health"),
    ("106", "Eczema"),
    ("107", "Heart Disease"),
    ("108", "Oral Health"),
    ("109", "Head"),
    ("110", "forehead"),
)


class Category(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='product_images')
    url = models.URLField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False, blank=False)
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='product_images')
    url = models.URLField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_category = models.CharField(
        max_length=20,
        choices=SUB_CATEGORY,
        default='101'
    )
    name = models.CharField(max_length=255, null=False, blank=False)
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='product_images')
    url = models.URLField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
