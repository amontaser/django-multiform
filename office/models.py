from django.db import models
from smart_selects.db_fields import ChainedForeignKey
from django.utils import timezone

class Country(models.Model):
    name = models.CharField(max_length=40, unique=True, blank=True, null=True)
    sortname = models.CharField(max_length=2, blank=True, null=True)
    
    class Meta:
        verbose_name_plural = 'Countries'
        ordering = ('name',)

    def __str__(self):
        return self.name

class Province(models.Model):
    name = models.CharField(max_length=165, blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='Province')

    class Meta:
        unique_together = ('name', 'country')   
        ordering = ('country', 'name')

    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField(max_length=165, blank=True, null=True)
    province = models.ForeignKey(Province, related_name='districts',on_delete=models.CASCADE,verbose_name='Province')

    class Meta:
        ordering = ('province', 'name')

    def __str__(self):
        return self.name


class Address(models.Model):
    address_line = models.CharField(max_length=60, blank=True, null=True)
    address_line2 = models.CharField(max_length=60, blank=True, null=True)
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    notes = models.CharField(max_length=150,blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='District', blank=True, null=True)
    province =ChainedForeignKey(Province,chained_field="country",chained_model_field="country",show_all=False,auto_choose=True,sort=True)
    district =ChainedForeignKey(District,chained_field="province",chained_model_field="province",show_all=False,auto_choose=True,sort=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    
    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Addresses"

    def full_address(self):
         return '{}, {}, {}, {}'.format(self.district.province.country.name, self.district.province.name, self.district.name, self.address_line)

    def __str__(self):
        return '{}, {}, {}, {}'.format(self.district.province.country.name, self.district.province.name, self.district.name, self.address_line)

class Office(models.Model):
    name = models.CharField(max_length=100,null=True)
    email = models.EmailField(verbose_name='Email Address',null=True,blank=True, unique=None, max_length=100)
    created = models.DateTimeField(auto_now_add=timezone.now())    
    updated = models.DateTimeField(auto_now=timezone.now()) 
    address = models.OneToOneField(Address, on_delete=models.CASCADE, related_name='officeAddress',null=True)

    def __str__(self):
        return self.name
