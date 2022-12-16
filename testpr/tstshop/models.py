import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _
from tstshop.fields import WEBPField

def image_folder(instance, filename):
    q = filename.split(".")[1]
    instance.formats = q
    if q in ['png', 'jpg', 'PNG', 'JPG']:
        return 'images/{}.webp'.format(uuid.uuid4().hex)

    return f'images/{filename}'

class Product(models.Model):
    st_opt = [("В наличии", "В наличии"), ("Под заказ", "Под заказ"), ("Ожидается поступление", "Ожидается поступление"),
              ("Нет в наличии", "Нет в наличии"), ("Не производится", "Не производится")]

    class Meta:
        verbose_name = _('product')
        verbose_name_plural = _('products')

        ordering = ['title']

    id = models.IntegerField(_('id'), unique=True, primary_key=True)
    title = models.CharField(_('title'), max_length=255)
    art = models.IntegerField(_('art'), unique=True)
    status = models.CharField(_('status'), max_length=255, choices=st_opt)

    def __str__(self):
        return self.title


class Image(models.Model):

    class Meta:
        verbose_name = _('image')

    prod_id = models.ForeignKey('Product', on_delete=models.PROTECT, max_length=255, related_name='image')
    #path = models.ImageField(_('path'), upload_to="images/product/")
    path = WEBPField(verbose_name=_('path'), upload_to=image_folder)
    formats = models.CharField(_('formats'), max_length=255)

    def __str__(self):
        return str(self.path)

