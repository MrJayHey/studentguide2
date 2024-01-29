from django.db import models
from django.utils.translation import gettext_lazy as _


class Hostel(models.Model):
    hostel_number = models.CharField(_("Hostel Number"), max_length=2)
    hostel_photo = models.ImageField(_("Hostel Photo"), upload_to='hostels/')
    price_for_scholarship = models.IntegerField(_("Price For Scholarship"))
    price_for_paid_basis = models.IntegerField(_("Price for paid basis"))
    floors = models.IntegerField(_("Floors"))
    gym = models.BooleanField(_("Gym"), default=False)
    type = models.CharField(_("Type"),max_length=128)
    coworking = models.BooleanField(_("Coworking"), default=False)
    kitchens = models.CharField(_("Kitchens"), max_length=32)
    washers = models.CharField(_("Washers"), max_length=32)
    adress = models.CharField(_("Address"), max_length=256)
    dryers = models.IntegerField(_("Dryers"))
    to_pryaniki = models.CharField(_("To Pryaniki"), max_length=64)
    to_pk = models.CharField(_("To PK"), max_length=64)
    to_bs = models.CharField(_("To BS"), max_length=64)
    to_mikhalka = models.CharField(_("To Mikhalka"), max_length=64)
    to_avtovaz = models.CharField(_("To Avtovaz"), max_length=64)
    
    def __str__(self):
        return f"Hostel {self.hostel_number}"
    
    
    