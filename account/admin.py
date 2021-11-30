from django.contrib import admin
from wallet.models import Wallet
from account.models import CustomUser
from shop.models import Category, Card
from django.forms import ModelForm, ValidationError
from django.utils.safestring import mark_safe

from PIL import Image


class CardAdminForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].help_text = mark_safe(f'<span style="color: coral; font-size: 12px">Load images with {Card.MIN_RESOLUTION[0]}x{Card.MIN_RESOLUTION[1]} resolution</span>')

    # def clean_image(self):
    #     image = self.cleaned_data['image']
    #     img = Image.open(image)
    #     if image.size > Card.MAX_IMAGE_SIZE:
    #         raise ValidationError(f"Image size can't be more than {(int)(Card.MAX_IMAGE_SIZE / 1048576)}MB")
    #     if img.width < Card.MIN_RESOLUTION[0] or img.height < Card.MIN_RESOLUTION[1]:
    #         raise ValidationError(f"Image resolution {img.width}x{img.height} is less the required")
    #     if img.width > Card.MAX_RESOLUTION[0] or img.height > Card.MAX_RESOLUTION[1]:
    #         raise ValidationError(f"Image resolution {img.width}x{img.height}  is bigger then the required")
    #     return image


admin.site.register(Wallet)
admin.site.register(CustomUser)
admin.site.register(Card)
admin.site.register(Category)
