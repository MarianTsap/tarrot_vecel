from django.db import models


class Cards(models.Model):
    card = models.ImageField(upload_to='cards/', blank=True, null=True)
    card_meaning = models.TextField()
    card_meaning_ukr = models.TextField()
