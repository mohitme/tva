from django.db import models

# Create your models here.
class EndUser(models.Model):
    first_name = models.TextField(verbose_name="First Name")
    last_name = models.TextField(verbose_name="Last Name")
    company_name = models.TextField(verbose_name="Company Name")
    city = models.TextField(verbose_name="City")
    state = models.TextField(verbose_name="State")
    web = models.TextField(verbose_name="Website")
    age = models.PositiveIntegerField(verbose_name="Age")
    zip = models.PositiveIntegerField(verbose_name="Zipcode")
    email = models.EmailField(verbose_name="Email Id", unique=True)


    class Meta:
        verbose_name = "EndUser"
        verbose_name_plural = "EndUsers"

    def __str__(self):
        return self.id
