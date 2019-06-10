from django.db import models

# Create your models here.


class DataSchema(models.Model):
    company_name = models.CharField(max_length=50)
    company_url = models.CharField(max_length=100)
    company_email = models.EmailField(max_length=50)
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    city_name = models.CharField(max_length=100)

    def __str__(self):
        return self.company_name

