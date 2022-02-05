from PIL import Image
from django.db import models

SUB_CATEGORY = (
    ("101", "Addiction"),
    ("102", "Beauty"),
    ("103", "Dental Health"),
    ("104", "Dietary Supplements"),
    ("105", "Diets & Weight Loss"),
    ("106", "Exercise & Fitness"),
    ("107", "General"),
    ("108", "Meditation"),
    ("109", "Men’s Health"),
    ("110", "Mental Health"),
    ("111", "Nutrition"),
    ("112", "Remedies"),
    ("113", "Sleep and Dreams"),
    ("114", "Spiritual Health"),
    ("115", "Strength Training"),
    ("116", "Women’s Health"),
    ("117", "Yoga"),
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
    affiliate_link = models.URLField(max_length=255)
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

    class Meta:
        ordering = ['-id']
