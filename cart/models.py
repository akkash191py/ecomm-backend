from django.db import models
from django.contrib.auth.models import User
from products.models import Product
from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver

# Cart
class Cart(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    total_price = models.FloatField(default=0)

    class Meta:
        verbose_name_plural='1. Cart'

    def __str__(self):
        return str(self.user.username) + " " + str(self.total_price)


# Cart Items
class CartItems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    isOrder = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)


    class Meta:
        verbose_name_plural='2. Cart Items'

    def __str__(self):
        return str(self.user.username) + " " + str(self.product.product_name)

# Signals for CartItems
@receiver(pre_save, sender=CartItems)
def correct_price(sender, **kwargs):
    cart_items = kwargs['instance']
    price_of_product = Product.objects.get(id=cart_items.product.id)
    cart_items.price = cart_items.quantity * float(price_of_product.price)
    #total_cart_items = CartItems.objects.filter(user= cart_items.user)
    #cart = Cart.objects.get(id = cart_items.cart.id)
    #cart.total_price = cart_items.price
    #cart.save()


# Order
class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    amount = models.FloatField(default=0)
    is_paid = models.BooleanField(default=False)
    order_id = models.CharField(max_length=100, blank=True)
    payment_id = models.CharField(max_length=100, blank=True)
    payment_signature = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name_plural='4. Orders'


# Ordered Items
class OrderedItems(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural='5. Orderd Items'




# Product Review
RATING = (
    (1,'1'),
    (2,'2'),
    (3,'3'),
    (4,'4'),
    (5,'5'),
)
class ProductReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    review_text = models.TextField(blank = True)
    review_rating = models.CharField(choices=RATING,max_length=150)


    class Meta:
        verbose_name_plural='3. Product Review'


