from PIL import Image
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    bank_name = models.CharField(max_length=255, null=True, blank=True)
    account_name = models.CharField(max_length=255, null=True, blank=True)
    account_number = models.CharField(max_length=255, null=True, blank=True)
    ifsc_code = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)

    google_pay_number = models.CharField(max_length=255, null=True, blank=True)
    google_pay_upi = models.CharField(max_length=255, null=True, blank=True)

    phone_pay_number = models.CharField(max_length=255, null=True, blank=True)
    phone_pay_upi = models.CharField(max_length=255, null=True, blank=True)

    paytm_number = models.CharField(max_length=255, null=True, blank=True)
    paytm_upi = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
