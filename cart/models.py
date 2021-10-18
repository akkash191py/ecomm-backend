from django.db import models
from django.utils.text import slugify

CATEGORY_CHOICES = (
    ('S','Shirt'),
    ('SW', 'Sport wear'),
    ('OW', 'Outwear')
)

LABEL_CHOICES = (
    ('P','primary'),
    ('S','secondary'),
    ('D','danger')
)


class Item(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    label = models.CharField(choices=LABEL_CHOICES, max_length=1)
    slug = models.SlugField()
    price = models.FloatField()
    description = models.TextField(blank=True, null=True)
    discount_price = models.FloatField(blank=True, null=True)
    image = models.ImageField()


    def __str__(self):
        return self.title