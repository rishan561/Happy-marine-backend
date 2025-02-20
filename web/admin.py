from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from web.models import AdminRegisterShipForSale,CstmUser,Category,Sub_category,Amenities,RegisterShipForSale,RegisterShipForCharter,RegisterShipForEquipments

# Register your models here.

class CustomAdmin(UserAdmin):
    list_display=['id','username','email','first_name','last_name','phone','image','is_active','address']
admin.site.register(CstmUser,CustomAdmin)

class CategoryAdmin(admin.ModelAdmin):
     list_display=['id','category_name','category_image','category_description']
admin.site.register(Category,CategoryAdmin) 

class SubCategoryAdmin(admin.ModelAdmin):
     list_display=['id','sub_category_name','category','sub_category_description']
admin.site.register(Sub_category,SubCategoryAdmin) 


class AmenitiesAdmin(admin.ModelAdmin):
     list_display=['id','amenities']
admin.site.register(Amenities,AmenitiesAdmin) 

class AdminRegShipForSaleAdmin(admin.ModelAdmin):
     list_display=['id','title','vessel_type','short_description','flag','year_built','capacity','LOA','Class','GRT_NRT','Teu','main_engine','DWT','Price','brief_description','email','phone','image','thumbnail_image','is_status','main_category','hidden_details']
admin.site.register(AdminRegisterShipForSale,AdminRegShipForSaleAdmin)

class RegShipForSaleAdmin(admin.ModelAdmin):
     list_display=['id','title','vessel_type','short_description','flag','year_built','capacity','LOA','Class','GRT_NRT','Teu','main_engine','DWT','Price','brief_description','email','phone','image','thumbnail_image','is_status','main_category']
admin.site.register(RegisterShipForSale,RegShipForSaleAdmin)


class RegShipForCharterAdmin(admin.ModelAdmin):
     list_display=['id','vessel_type','short_description','nationality','inspection_country','year_built','desirable_capacity','buy_as_scrap','Class','from_price','to_price','brief_description','email','phone','image','is_status']
admin.site.register(RegisterShipForCharter,RegShipForCharterAdmin)


class RegShipForEquipmentsAdmin(admin.ModelAdmin):
     list_display=['id','category','subject','brief_description','email','phone','is_status']
admin.site.register(RegisterShipForEquipments,RegShipForEquipmentsAdmin)