from rest_framework import serializers
from web.models import AdminRegisterShipForSale,CstmUser,Category,Sub_category,Amenities,RegisterShipForSale,RegisterShipForCharter,RegisterShipForEquipments,Amenity

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model=CstmUser
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Sub_category
        fields = '__all__'

class AmenitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenities
        fields = '__all__'


    
class AmenitYSerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenity
        fields = '__all__'

class RegSgipForSaleSerializer(serializers.ModelSerializer):
    amenities = AmenitYSerializer(many=True, required=False)  # Nested serializer

    class Meta:
        model = AdminRegisterShipForSale
        fields = '__all__'

    def create(self, validated_data):
        amenities_data = validated_data.pop('amenities', [])  # Extract amenities data
        ship = AdminRegisterShipForSale.objects.create(**validated_data)
        
        # Save amenities linked to the ship
        for amenity_data in amenities_data:
            Amenity.objects.create(ship=ship, **amenity_data)
        
        return ship

class RegisterShipForSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisterShipForSale
        fields = '__all__'

class RegisterShipForCharterSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisterShipForCharter
        fields = '__all__'

class RegisterShipForEquipmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisterShipForEquipments
        fields = '__all__'