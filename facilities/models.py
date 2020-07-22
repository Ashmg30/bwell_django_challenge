from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.


@python_2_unicode_compatible
class Description(models.Model):
    #facility_id = models.ForeignKey(Facility, default=1, verbose_name="Facilities", on_delete=models.CASCADE)
    short_description = models.TextField(null=True)
    description = models.TextField(max_length=200,blank=True, default='',null=True)
    
    class Meta:
        verbose_name_plural = "Description"
    
    def __str__(self):
        return str(self.id) + "\t" +self.short_description

@python_2_unicode_compatible
class Address(models.Model):
    #facility_id = models.ForeignKey(Facility, default=1, verbose_name="Facilities", on_delete=models.CASCADE)
    facility_address_one = models.CharField(max_length=200,blank=True, default='',null=True)
    facility_address_two = models.CharField(max_length=200,blank=True, default='',null=True)
    facility_city = models.CharField(max_length=200,blank=True, default='',null=True)
    facility_state = models.CharField(max_length=200,blank=True, default='',null=True)
    facility_zip_code = models.CharField(max_length=200,blank=True, default='',null=True)
    facility_latitude = models.CharField(max_length=200,blank=True, default='',null=True)
    facility_longitude = models.CharField(max_length=200,blank=True, default='',null=True)
    facility_location = models.CharField(max_length=200,blank=True, default='',null=True)
    facility_country_code = models.CharField(max_length=200,blank=True, default='',null=True)
    facility_country = models.CharField(max_length=200,blank=True, default='',null=True)
    
    class Meta:
        verbose_name_plural = "Address"
    
    def __str__(self):
        return str(self.id)+ "\t" +self.facility_address_one

@python_2_unicode_compatible
class Facility(models.Model):
    facility_id = models.PositiveIntegerField()
    facility_name = models.CharField(max_length=200,blank=True, default='',null=True)
    facility_phone_number = models.CharField(max_length=200,blank=True, default='',null=True)
    facility_open = models.DateField(auto_now_add=False, auto_now=False, blank=True,null=True)
    facility_fax_number = models.CharField(max_length=200,blank=True, default='',null=True)
    main_site_facility_id = models.CharField(max_length=200,blank=True, default='',null=True)
    description = models.ForeignKey(Description, default=1, verbose_name="Description", on_delete=models.CASCADE)
    address = models.ForeignKey(Address, default=1, verbose_name="Address", on_delete=models.CASCADE)
   
    class Meta:
        verbose_name_plural = "Facilities"

    def __str__(self):
        return str(self.facility_name)

