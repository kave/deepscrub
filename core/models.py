from django.db import models


class Price(models.Model):
    cost = models.FloatField(blank=False)
    promotion = models.CharField(max_length=100, blank=False)

    def __unicode__(self):
        return '${0}'.format(self.cost)


class Color(models.Model):
    WHITE = 1
    BLACK = 2
    name = models.CharField(max_length=50, blank=False)
    type = models.IntegerField(blank=False, default=0, unique=True)

    COLORS = {
        WHITE: 'White',
        BLACK: 'Black',
    }

    def __unicode__(self):
        return self.name


class SpongeType(models.Model):
    STRONG = 1
    GENTLE = 2
    name = models.CharField(max_length=50, blank=False)
    type = models.IntegerField(blank=False, unique=True)

    TYPES = {
        STRONG: 'Strong',
        GENTLE: 'Gentle',
    }

    def __unicode__(self):
        return self.name


class Sponge(models.Model):
    color = models.ForeignKey(Color)
    type = models.ForeignKey(SpongeType)
    quantity = models.IntegerField(blank=False, default=0)
    price = models.ForeignKey(Price)
    img_url = models.URLField(blank=True)

    class Meta:
        unique_together = ('color', 'type',)

    def __unicode__(self):
        return '{0}:{1}    #{2} {3}'.format(self.color, self.type, self.quantity, self.price)


class Receipt(models.Model):
    sponges = models.ManyToManyField(Sponge, related_name='receipt_sponges_set')

    name_shipping = models.CharField(max_length=100, blank=False)
    street1_shipping = models.CharField(max_length=200, blank=False)
    street2_shipping = models.CharField(max_length=200, blank=False)
    city_shipping = models.CharField(max_length=50, blank=False)
    state_shipping = models.CharField(max_length=50, blank=False)
    zipcode_shipping = models.CharField(max_length=20, blank=False)

    quantity = models.IntegerField(blank=False)
    shipping_cost = models.FloatField(blank=False)
    total_cost = models.FloatField(blank=False)


class Order(models.Model):
    receipt = models.ForeignKey(Receipt)


class ContactUs(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(blank=False)
    message = models.TextField(max_length=500, blank=False)

    def __unicode__(self):
        return self.message

    class Meta:
        verbose_name = "Contact Us"
        verbose_name_plural = "Contact Us"
