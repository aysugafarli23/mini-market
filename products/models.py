from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.
class Products(models.Model):
    owner = models.ForeignKey(User, on_delete = models.CASCADE)
    name = models.CharField(max_length=200, verbose_name="Məhsulun adı")
    endusedate = models.DateField(verbose_name="Son istifadə tarixi")
    orderduration = models.DurationField(verbose_name="Çatdırılma müddəti")
    originalprice = models.IntegerField(verbose_name="Məhsulun dəyəri")
    sellingprice = models.IntegerField( verbose_name="Məhsulun satış qiyməti")
    value = models.IntegerField(verbose_name="Qazanc", blank=True, null=True),
    slug = models.SlugField(unique=True, blank=True, null=True)
    
    def save (self,*args, **kwargs ):
        self.slug = slugify(self.name)
        self.value = int(self.sellingprice - self.originalprice)
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f'{self.owner.username.capitalize()} ----- {self.name}' 
    