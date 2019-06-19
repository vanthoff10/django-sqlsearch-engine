from django.db import models

# Create your models here.


class DataSchema(models.Model):
<<<<<<< HEAD
    company_name = models.CharField(max_length=100)
    company_url = models.CharField(max_length=200)
    company_email = models.EmailField(max_length=200)
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    city_name = models.CharField(max_length=100)

    def __str__(self):
        return self.company_name
=======
    company_name = models.CharField(max_length=50)
    company_url = models.CharField(max_length=100)
    company_email = models.EmailField(max_length=50)
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    city_name = models.CharField(max_length=100)

    def __str__(self):
        return True
>>>>>>> 4ff1fdf2c7e84dd487e5244af494e6b32072dc1f


class FormData(models.Model):
    lead_gen = models.CharField(max_length=50)
    company_name = models.CharField(max_length=100)
    company_address = models.CharField(max_length=200)
    company_city = models.CharField(max_length=100)
    company_state = models.CharField(max_length=100)
    company_country = models.CharField(max_length=100)
    company_url = models.CharField(max_length=100)
    company_linkedin = models.CharField(max_length=100)
    company_phone = models.CharField(max_length=100)
    company_email = models.CharField(max_length=100)
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    owner_linkedin = models.CharField(max_length=100)
    owner_title = models.CharField(max_length=100)
    owner_twitter = models.CharField(max_length=100)



