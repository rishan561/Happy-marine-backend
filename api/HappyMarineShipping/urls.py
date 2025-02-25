from django.urls import path
from api.HappyMarineShipping import views


urlpatterns = [
 path('RegShipForSale',views.AddShip),
 path('viewShip',views.AllShips),
 path('single/<int:id>',views.SingleShip),
 path('singleAmenity/<int:id>',views.SingleAmenity),

 path('updateShip/<int:id>',views.UpdateShip),
 path('deleteShip/<int:id>',views.DeleteShip),
 path('login',views.Login),

 path('AddShipForSale',views.AddShipForSale),
 path('viewShipForSale',views.ViewShipForSale),
 path('deleteShipForSale/<int:id>',views.DeleteShipForSale),

 path('RegShipForCharter',views.AddCharter),
 path('viewShipForCharter',views.ViewShipForCharter),
 path('deleteCharter/<int:id>',views.DeleteShipForCharter),

 path('RegShipForEquipments',views.AddEquipments),
 path('viewShipForEquipments',views.ViewShipForEquipments),
 path('deleteEquipments/<int:id>',views.DeleteShipForEquipments),

 path('AddAmenities',views.AddAmenities),
 path('viewAmenities',views.ViewAmenities),
 path('deleteAmenities/<int:id>',views.DeleteAmenities),
 path('updateAmenities/<int:id>',views.UpdateAmenities),
  path('singleAm/<int:id>',views.SingleAm),



 path('addCategory',views.AddCategory),
 path('viewCategory',views.AllCategory),
 path('updateCategory/<int:id>',views.UpdateCategory),
 path('deleteCategory/<int:id>',views.DeleteCat),

 path('addSubCategory',views.AddSubCategory),
 path('viewSubCategory',views.AllSubCategory),
 path('updateSubCategory/<int:id>',views.UpdateSubCategory),
 path('singleSubCat/<int:id>',views.SingleSubCat),
 path('deleteSubCategory/<int:id>',views.DeleteSubCat),

 path('users/admin',views.get_admin_user),
 path('singleAdmin',views.SingleAdmin),
 path('users/admin/update',views.UpdateUser),
 path('changePassA',views.ChangepassA),


 path('status/update/<int:id>',views.StatusU),
 path('statusD/update/<int:id>',views.StatusD),







]

