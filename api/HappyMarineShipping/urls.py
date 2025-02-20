from django.urls import path
from api.HappyMarineShipping import views


urlpatterns = [
 path('RegShipForSale',views.AddShip),
 path('viewShip',views.AllShips),
 path('single/<int:id>',views.SingleShip),
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





 path('addCategory',views.AddCategory),
 path('viewCategory',views.AllCategory),
 path('updateCategory/<int:id>',views.UpdateCategory),
 path('deleteCategory/<int:id>',views.DeleteCat),

 path('addSubCategory',views.AddSubCategory),
 path('viewSubCategory',views.AllSubCategory),
 path('updateSubCategory/<int:id>',views.UpdateSubCategory),
 path('singleSubCat/<int:id>',views.SingleSubCat),
 path('deleteSubCategory/<int:id>',views.DeleteSubCat),





]

