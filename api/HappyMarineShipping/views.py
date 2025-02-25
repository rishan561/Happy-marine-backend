from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response
from django.core.mail import send_mail
from django.conf import settings
import random
from django.utils.timezone import now,localtime

from .serializers import RegSgipForSaleSerializer,CategorySerializer,SubCategorySerializer,AmenitiesSerializer,RegisterShipForSaleSerializer,RegisterShipForCharterSerializer,RegisterShipForEquipmentsSerializer,AmenitYSerializer,userSerializer
from web.models import AdminRegisterShipForSale,CstmUser,Category,Sub_category,Amenities,RegisterShipForSale,RegisterShipForCharter,RegisterShipForEquipments,Amenity
from django.contrib.auth.hashers import make_password


from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

@api_view(['POST'])
@permission_classes([AllowAny])
def AddShip(request):
    data = request.data
    ship = RegSgipForSaleSerializer(data=data)
    print(data)

    # Extract amenities from the request
    amenities_data = {
        key.split("[")[1][:-1]: value[0]  # Extract the key inside brackets
        for key, value in data.lists() if key.startswith('value[') and value[0]  # Skip empty values
    }

    if ship.is_valid():
        saved_ship = ship.save()

        # Save amenities if they have non-empty values
        for name, value in amenities_data.items():
            if value.strip():  # Ensure the value is not empty
                Amenity.objects.create(ship=saved_ship, name=name, value=value)

        response_data = {
            "status": 200,
            "message": "Ship registered successfully"
        }
    else:
        print(ship.errors)
        response_data = {
            "status": 201,
            "message": "Data not added",
            "errors": ship.errors
        }

    return Response(response_data)


@api_view(['POST'])
@permission_classes([AllowAny])
def AddCharter(request):
   data=request.data
   ship=RegisterShipForCharterSerializer(data=data)
   print(data)
   if ship.is_valid():
        ship.save()
        response_data={
            "status":200,
            "message":"Charter registered Successfully"
        }
   else:
       response_data={
            "Status":201,
            "message":"data not Added"
        }
   return Response(response_data)

@api_view(['POST'])
@permission_classes([AllowAny])
def AddEquipments(request):
   data=request.data
   ship=RegisterShipForEquipmentsSerializer(data=data)
   print(data)
   if ship.is_valid():
        ship.save()
        response_data={
            "status":200,
            "message":"Equipment registered Successfully"
        }
   else:
       response_data={
            "Status":201,
            "message":"data not Added"
        }
   return Response(response_data)


@api_view(['POST'])
@permission_classes([AllowAny])
def AddShipForSale(request):
   data=request.data
   ship=RegisterShipForSaleSerializer(data=data)
   print(data)
   if ship.is_valid():
        ship.save()
        response_data={
            "status":200,
            "message":"Ship registered Successfully"
        }
   else:
       response_data={
            "Status":201,
            "message":"data not Added"
        }
   return Response(response_data)



@api_view(['GET'])
@permission_classes([AllowAny])
def AllShips(request):
    title=request.GET.get('title')
    context={
        "request":request
    }
    if title:
        ships = AdminRegisterShipForSale.objects.filter(title__icontains=title)
    else:
        ships = AdminRegisterShipForSale.objects.all()  
    serializer = RegSgipForSaleSerializer(instance=ships, many=True,context=context)
    if serializer:
        response_data = {
        "status": 200,
        "data": serializer.data
        }
    else:
            response_data = {
            "Status": 201,
            "message": "data not found",
            }
    return Response(response_data)


@api_view(['GET'])
@permission_classes([AllowAny])
def ViewShipForSale(request):
    title=request.GET.get('title')
    context={
        "request":request
    }
    if title:
        ships = RegisterShipForSale.objects.filter(title__icontains=title)
    else:
        ships = RegisterShipForSale.objects.all()  
    serializer = RegisterShipForSaleSerializer(instance=ships, many=True,context=context)
    if serializer:
        response_data = {
        "status": 200,
        "data": serializer.data
        }
    else:
            response_data = {
            "Status": 201,
            "message": "data not found",
            }
    return Response(response_data)


@api_view(['GET'])
@permission_classes([AllowAny])
def ViewShipForCharter(request):
    short_description=request.GET.get('short_description')
    context={
        "request":request
    }
    if short_description:
        ships = RegisterShipForCharter.objects.filter(short_description__icontains=short_description)
    else:
        ships = RegisterShipForCharter.objects.all()  
    serializer = RegisterShipForCharterSerializer(instance=ships, many=True,context=context)
    if serializer:
        response_data = {
        "status": 200,
        "data": serializer.data
        }
    else:
            response_data = {
            "Status": 201,
            "message": "data not found",
            }
    return Response(response_data)

@api_view(['GET'])
@permission_classes([AllowAny])
def ViewShipForEquipments(request):
    category=request.GET.get('category')
    context={
        "request":request
    }
    if category:
        ships = RegisterShipForEquipments.objects.filter(category__icontains=category)
    else:
        ships = RegisterShipForEquipments.objects.all()  
    serializer = RegisterShipForEquipmentsSerializer(instance=ships, many=True,context=context)
    if serializer:
        response_data = {
        "status": 200,
        "data": serializer.data
        }
    else:
            response_data = {
            "Status": 201,
            "message": "data not found",
            }
    return Response(response_data)



@api_view(['GET'])
@permission_classes([AllowAny])
def SingleShip(request,id):
    context={
        "request":request
    }
    if AdminRegisterShipForSale.objects.get(id=id):
      ship=AdminRegisterShipForSale.objects.get(id=id)
      serializer=RegSgipForSaleSerializer(instance=ship,context=context)
      if serializer:
            response_data={
                "status":200,
                "data":serializer.data
            }
      else:
            response_data={
                "status":201,
                "message":"data not found"
            }  
    else:
        response_data={
                "status":201,
                "message":f"Ship with id {id} does not exist"
            }  
    return Response(response_data)



@api_view(['GET'])
@permission_classes([AllowAny])
def SingleAmenity(request, id):
    context = {"request": request}

    # Get all amenities related to the ship
    amenities = Amenity.objects.filter(ship_id=id)

    if amenities.exists():
        serializer = AmenitYSerializer(amenities, many=True, context=context)
        response_data = {
            "status": 200,
            "data": serializer.data
        }
    else:
        response_data = {
            "status": 404,
            "message": f"No amenities found for ship with id {id}"
        }

    return Response(response_data)



@api_view(['GET'])
@permission_classes([AllowAny])
def SingleAm(request,id):
    context={
        "request":request
    }
    if Amenities.objects.get(id=id):
      ship=Amenities.objects.get(id=id)
      serializer=AmenitiesSerializer(instance=ship,context=context)
      if serializer:
            response_data={
                "status":200,
                "data":serializer.data
            }
      else:
            response_data={
                "status":201,
                "message":"data not found"
            }  
    else:
        response_data={
                "status":201,
                "message":f"Ship with id {id} does not exist"
            }  
    return Response(response_data)



@api_view(['POST'])
@permission_classes([AllowAny])
def Login(request):
    login_input = request.data.get('email')  # This can be email or username
    password = request.data.get('password')

    # Check if input is email or username
    user = CstmUser.objects.filter(email=login_input).first()  # Try finding user by email

    if user is None:
        user = CstmUser.objects.filter(username=login_input).first()  # Try username

    if user and user.check_password(password):
        token, created = Token.objects.get_or_create(user=user)
        response_data = {
            'status': 200,
            'token': token.key,
            'is_admin': user.is_staff,
        }
    else:
        response_data = {
            'status': 201,
            'message': "Username or Password doesn't match",
        }

    return Response(response_data)



@api_view(['POST'])
@permission_classes([AllowAny])
def AddCategory(request):
   data=request.data
   category=CategorySerializer(data=data)
   print(data)
   if category.is_valid():
        category.save()
        response_data={
            "status":200,
            "message":"category added Successfully"
        }
   else:
       response_data={
            "Status":201,
            "message":"data not Added"
        }
   return Response(response_data)


@api_view(['GET'])
@permission_classes([AllowAny])
def AllCategory(request):
    category_name=request.GET.get('category_name')
    context={
        "request":request
    }
    if category_name:
        category = Category.objects.filter(category_name__icontains=category_name)
    else:
        category = Category.objects.all()  
    serializer = CategorySerializer(instance=category, many=True,context=context)
    if serializer:
        response_data = {
        "status": 200,
        "data": serializer.data
        }
    else:
            response_data = {
            "Status": 201,
            "message": "data not found",
            }
    return Response(response_data)


@api_view(['PUT'])
@permission_classes([AllowAny])
def UpdateCategory(request,id):
   instance=Category.objects.get(id=id)
   data=request.data.copy()
   department=CategorySerializer(instance=instance,data=data,partial=True)
   if department.is_valid():
        department.save()
        response_data={
            "status":200,
            "message":"Updated Successfully"
        }
   else:
       response_data={
            "status":201,
            "message":"data not found"
        }
   return Response(response_data)


@api_view(['DELETE'])
@permission_classes([AllowAny])
def DeleteCat(request,id):
   category=Category.objects.get(id=id)
   if category:
        category.delete()
        response_data={
            "status":200,
            "message":"success"
        }
   else:
       response_data={
            "status":201,
            "message":"data not found"
        }
   return Response(response_data)



@api_view(['POST'])
@permission_classes([AllowAny])
def AddSubCategory(request):
   data=request.data
   category=SubCategorySerializer(data=data)
   print(data)
   if category.is_valid():
        category.save()
        response_data={
            "status":200,
            "message":"category added Successfully"
        }
   else:
       response_data={
            "Status":201,
            "message":"data not Added"
        }
   return Response(response_data)


@api_view(['GET'])
@permission_classes([AllowAny])
def AllSubCategory(request):
    sub_category_name=request.GET.get('sub_category_name')
    context={
        "request":request
    }
    if sub_category_name:
        category = Sub_category.objects.filter(sub_category_name__icontains=sub_category_name)
    else:
        category = Sub_category.objects.all()  
    serializer = SubCategorySerializer(instance=category, many=True,context=context)
    if serializer:
        response_data = {
        "status": 200,
        "data": serializer.data
        }
    else:
            response_data = {
            "Status": 201,
            "message": "data not found",
            }
    return Response(response_data)


@api_view(['GET'])
@permission_classes([AllowAny])
def SingleSubCat(request,id):
    context={
        "request":request
    }
    if Sub_category.objects.get(id=id):
      ship=Sub_category.objects.get(id=id)
      serializer=SubCategorySerializer(instance=ship,context=context)
      if serializer:
            response_data={
                "status":200,
                "data":serializer.data
            }
      else:
            response_data={
                "status":201,
                "message":"data not found"
            }  
    else:
        response_data={
                "status":201,
                "message":f"Ship with id {id} does not exist"
            }  
    return Response(response_data)


@api_view(['PUT'])
@permission_classes([AllowAny])
def UpdateSubCategory(request,id):
   instance=Sub_category.objects.get(id=id)
   data=request.data.copy()
   department=SubCategorySerializer(instance=instance,data=data,partial=True)
   if department.is_valid():
        department.save()
        response_data={
            "status":200,
            "message":"Updated Successfully"
        }
   else:
       response_data={
            "status":201,
            "message":"data not found"
        }
   return Response(response_data)



@api_view(['DELETE'])
@permission_classes([AllowAny])
def DeleteSubCat(request,id):
   category=Sub_category.objects.get(id=id)
   if category:
        category.delete()
        response_data={
            "status":200,
            "message":"success"
        }
   else:
       response_data={
            "status":201,
            "message":"data not found"
        }
   return Response(response_data)



@api_view(['PUT'])
@permission_classes([AllowAny])
def UpdateShip(request, id):
    try:
        # Get the ship instance
        instance = AdminRegisterShipForSale.objects.get(id=id)
        data = request.data.copy()  # ✅ Make a single mutable copy

        # ✅ Handle empty image and thumbnail_image
        if data.get('image') == "" and instance.image:
            data['image'] = instance.image  # Keep current image

        if data.get('thumbnail_image') == "" and instance.thumbnail_image:
            data['thumbnail_image'] = instance.thumbnail_image  # Keep current thumbnail image

        # Deserialize and update ship
        department = RegSgipForSaleSerializer(instance=instance, data=data, partial=True)

        if department.is_valid():
            department.save()

            # ✅ Extract amenities data from request
            amenities_data = {
                key.split("[")[1][:-1]: value[0]  # Extract name from "value[name]"
                for key, value in data.lists() if key.startswith('value[') and value[0]
            }

            # ✅ Update or create amenities
            for name, value in amenities_data.items():
                if value.strip():  # Ensure value is not empty
                    Amenity.objects.update_or_create(
                        ship=instance,
                        name=name,
                        defaults={'value': value}
                    )

            response_data = {
                "status": 200,
                "message": "Updated Successfully"
            }
        else:
            response_data = {
                "status": 201,
                "message": "Data not found",
                "errors": department.errors
            }

    except AdminRegisterShipForSale.DoesNotExist:
        response_data = {
            "status": 404,
            "message": "Ship not found"
        }

    return Response(response_data)

    return Response(response_data)


@api_view(['DELETE'])
@permission_classes([AllowAny])
def DeleteShip(request,id):
   category=AdminRegisterShipForSale.objects.get(id=id)
   if category:
        category.delete()
        response_data={
            "status":200,
            "message":"success"
        }
   else:
       response_data={
            "status":201,
            "message":"data not found"
        }
   return Response(response_data)

@api_view(['DELETE'])
@permission_classes([AllowAny])
def DeleteShipForSale(request,id):
   category=RegisterShipForSale.objects.get(id=id)
   if category:
        category.delete()
        response_data={
            "status":200,
            "message":"success"
        }
   else:
       response_data={
            "status":201,
            "message":"data not found"
        }
   return Response(response_data)

@api_view(['DELETE'])
@permission_classes([AllowAny])
def DeleteShipForCharter(request,id):
   category=RegisterShipForCharter.objects.get(id=id)
   if category:
        category.delete()
        response_data={
            "status":200,
            "message":"success"
        }
   else:
       response_data={
            "status":201,
            "message":"data not found"
        }
   return Response(response_data)

@api_view(['DELETE'])
@permission_classes([AllowAny])
def DeleteShipForEquipments(request,id):
   category=RegisterShipForEquipments.objects.get(id=id)
   if category:
        category.delete()
        response_data={
            "status":200,
            "message":"success"
        }
   else:
       response_data={
            "status":201,
            "message":"data not found"
        }
   return Response(response_data)


@api_view(['POST'])
@permission_classes([AllowAny])
def AddAmenities(request):
   data=request.data
   ship=AmenitiesSerializer(data=data)
   print(data)
   if ship.is_valid():
        ship.save()
        response_data={
            "status":200,
            "message":"amenities registered Successfully"
        }
   else:
       response_data={
            "Status":201,
            "message":"data not Added"
        }
   return Response(response_data)


@api_view(['GET'])
@permission_classes([AllowAny])
def ViewAmenities(request):
    amenities=request.GET.get('amenities')
    context={
        "request":request
    }
    if amenities:
        ships = Amenities.objects.filter(amenities__icontains=amenities)
    else:
        ships = Amenities.objects.all()  
    serializer = AmenitiesSerializer(instance=ships, many=True,context=context)
    if serializer:
        response_data = {
        "status": 200,
        "data": serializer.data
        }
    else:
            response_data = {
            "Status": 201,
            "message": "data not found",
            }
    return Response(response_data)


@api_view(['DELETE'])
@permission_classes([AllowAny])
def DeleteAmenities(request,id):
   category=Amenities.objects.get(id=id)
   if category:
        category.delete()
        response_data={
            "status":200,
            "message":"success"
        }
   else:
       response_data={
            "status":201,
            "message":"data not found"
        }
   return Response(response_data)


@api_view(['PUT'])
@permission_classes([AllowAny])
def UpdateAmenities(request,id):
   instance=Amenities.objects.get(id=id)
   data=request.data
   department=AmenitiesSerializer(instance=instance,data=data,partial=True)
   if department.is_valid():
        department.save()
        response_data={
            "status":200,
            "message":"Updated Successfully"
        }
   else:
       response_data={
            "status":201,
            "message":"data not found"
        }
   return Response(response_data)



@api_view(['GET'])
@permission_classes([AllowAny])
def get_admin_user(request):
    try:
        admin_user = CstmUser.objects.filter(is_superuser=True).first()  # Use this or role='admin'
        if admin_user:
            serializer = userSerializer(admin_user)
            return Response({"status": 200, "data": serializer.data})
        else:
            return Response({"status": 404, "message": "Admin user not found"})
    except Exception as e:
        return Response({"status": 500, "message": str(e)})


@api_view(['GET'])
@permission_classes([AllowAny])
def SingleAdmin(request,id):
    context={
        "request":request
    }
    if CstmUser.objects.get(id=id):
      ship=CstmUser.objects.get(id=id)
      serializer=userSerializer(instance=ship,context=context)
      if serializer:
            response_data={
                "status":200,
                "data":serializer.data
            }
      else:
            response_data={
                "status":201,
                "message":"data not found"
            }  
    else:
        response_data={
                "status":201,
                "message":f"Ship with id {id} does not exist"
            }  
    return Response(response_data)


from rest_framework import status
from django.shortcuts import get_object_or_404

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def UpdateUser(request):
    # Get the user from the token
    instance = request.user
    data = request.data.copy()

    # Update image from FILES if provided
    if 'image' in request.FILES:
        instance.image = request.FILES['image']

    # Update other fields
    instance.company_name = data.get('company_name', instance.company_name)
    instance.email = data.get('email', instance.email)
    instance.phone = data.get('phone', instance.phone)
    instance.address = data.get('address', instance.address)

    # Handle password change if provided
    old_password = data.get('old_password')
    new_password = data.get('new_password')

    if old_password and new_password:
        if instance.check_password(old_password):
            instance.set_password(new_password)
        else:
            return Response({
                "status": 401,
                "message": "Old password is not correct."
            }, status=401)

    instance.save()

    response_data = {
        "status": status.HTTP_200_OK,
        "message": "User updated successfully",
        "data": {
            "company_name": instance.company_name,
            "email": instance.email,
            "phone": instance.phone,
            "address": instance.address,
            "image": str(instance.image.url) if instance.image else None
        }
    }

    return Response(response_data, status=status.HTTP_200_OK)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def ChangepassA(request):
    user = request.user
    old_password = request.data.get('old_password')
    new_password = request.data.get('new_password')

    if not old_password or not new_password:
        return Response({
            'status': 400,
            'message': 'Both old and new passwords are required.'
        }, status=400)

    if user.check_password(old_password):
        user.set_password(new_password)
        user.save()
        return Response({
            'status': 200,
            'message': 'Password changed successfully.'
        })
    else:
        return Response({
            'status': 401,
            'message': 'Old password is not correct.'
        }, status=401)



@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def StatusU(request,id):
    instance=AdminRegisterShipForSale.objects.get(id=id)

    status=RegSgipForSaleSerializer(instance,data={'is_status':True},partial=True)
    if status.is_valid():
        status.save()
        response_data={
            "status":200,
            "message":'success'
        }
    else:
        response_data={
            "status":201,
            "message":"error"
        }
    return Response(response_data)  


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def StatusD(request,id):
    instance=AdminRegisterShipForSale.objects.get(id=id)

    status=RegSgipForSaleSerializer(instance,data={'is_status':False},partial=True)
    if status.is_valid():
        status.save()
        response_data={
            "status":200,
            "message":'success'
        }
    else:
        response_data={
            "status":201,
            "message":"error"
        }
    return Response(response_data)  