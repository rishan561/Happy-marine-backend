from django.db import models
from django.contrib.auth.models import AbstractUser

class CstmUser(AbstractUser):
    phone=models.DecimalField(decimal_places=0,max_digits=10,null=True)
    image=models.ImageField(upload_to='user_image',blank=True,null=True)
    address=models.TextField(null=True,blank=True)

class Category(models.Model):
    category_name = models.CharField(max_length=100)
    category_image = models.ImageField(upload_to='category_image',blank=True,null=True)
    category_description = models.TextField(null=True,blank=True)


class Sub_category(models.Model):
    sub_category_name = models.CharField(max_length=100)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
    sub_category_description = models.TextField(null=True,blank=True)

class Amenities(models.Model):
    amenities = models.CharField(max_length=100)

class AdminRegisterShipForSale(models.Model): 
    title = models.CharField(max_length=100,null=True,blank=True)
    vessel_type = models.CharField(max_length=100,null=True,blank=True)
    short_description = models.TextField(null=True,blank=True)
    flag = models.CharField(max_length=100,null=True,blank=True)
    year_built = models.DecimalField(decimal_places=0,max_digits=4,null=True,blank=True)
    capacity = models.CharField(max_length=100,null=True,blank=True)
    LOA = models.CharField(max_length=100,null=True,blank=True)
    Class = models.CharField(max_length=100,null=True,blank=True)
    GRT_NRT = models.CharField(max_length=100, null=True,blank=True)
    Teu = models.CharField(max_length=100,null=True,blank=True)
    main_engine = models.CharField(max_length=100,null=True,blank=True)
    DWT = models.CharField(max_length=100,null=True,blank=True)
    Price = models.CharField(max_length=100,null=True,blank=True)
    brief_description = models.TextField(null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    phone = models.DecimalField(decimal_places=0,max_digits=10,null=True,blank=True)
    image=models.ImageField(upload_to='ship_image',blank=True,null=True)
    thumbnail_image=models.ImageField(upload_to='ship_image',blank=True,null=True)
    is_status=models.BooleanField(default=False)
    main_category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
    hidden_details = models.TextField(null=True,blank=True)
    


class Amenity(models.Model):
    ship = models.ForeignKey(AdminRegisterShipForSale, on_delete=models.CASCADE, related_name='amenities')  # Ensure this field exists
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=255)

class RegisterShipForSale(models.Model): 
    title = models.CharField(max_length=100,null=True,blank=True)
    vessel_type = models.CharField(max_length=100,null=True,blank=True)
    short_description = models.TextField(null=True,blank=True)
    flag = models.CharField(max_length=100,null=True,blank=True)
    year_built = models.DecimalField(decimal_places=0,max_digits=4,null=True,blank=True)
    capacity = models.CharField(max_length=100,null=True,blank=True)
    LOA = models.CharField(max_length=100,null=True,blank=True)
    Class = models.CharField(max_length=100,null=True,blank=True)
    GRT_NRT = models.CharField(max_length=100, null=True,blank=True)
    Teu = models.CharField(max_length=100,null=True,blank=True)
    main_engine = models.CharField(max_length=100,null=True,blank=True)
    DWT = models.CharField(max_length=100,null=True,blank=True)
    Price = models.CharField(max_length=100,null=True,blank=True)
    brief_description = models.TextField(null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    phone = models.DecimalField(decimal_places=0,max_digits=10,null=True,blank=True)
    image=models.ImageField(upload_to='ship_image',blank=True,null=True)
    thumbnail_image=models.ImageField(upload_to='thumbnail_image',blank=True,null=True)
    is_status=models.BooleanField(default=False)
    main_category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
    

class RegisterShipForCharter(models.Model): 
    vessel_type = models.CharField(max_length=100,null=True,blank=True)
    short_description = models.TextField(null=True,blank=True)
    nationality = models.CharField(max_length=100,null=True,blank=True)
    inspection_country = models.CharField(max_length=100,null=True,blank=True)
    year_built = models.DecimalField(decimal_places=0,max_digits=4,null=True,blank=True)
    desirable_capacity = models.CharField(max_length=100,null=True,blank=True)
    Class = models.CharField(max_length=100,null=True,blank=True)
    buy_as_scrap = models.CharField(max_length=100, null=True,blank=True)
    from_price = models.CharField(max_length=100,null=True,blank=True)
    to_price = models.CharField(max_length=100,null=True,blank=True)
    brief_description = models.TextField(null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    phone = models.DecimalField(decimal_places=0,max_digits=10,null=True,blank=True)
    image=models.ImageField(upload_to='ship_image',blank=True,null=True)
    is_status=models.BooleanField(default=False)
    
    
class RegisterShipForEquipments(models.Model): 
    category = models.CharField(max_length=100,null=True,blank=True)
    subject = models.CharField(max_length=100,null=True,blank=True)
    brief_description = models.TextField(null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    phone = models.DecimalField(decimal_places=0,max_digits=10,null=True,blank=True)
    is_status=models.BooleanField(default=False)
    
    
