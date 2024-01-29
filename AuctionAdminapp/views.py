from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from AuctionAdminapp.serializers import ProductSerializer
from AuctionAdminapp.models import Product
from AuctionAdminapp.serializers import UserSerializer
from AuctionAdminapp.models import User

@csrf_exempt
def productApi(request,id=0):
    if request.method=='GET':
        product = Product.objects.all()
        product_serializer=ProductSerializer(product,many=True)
        return JsonResponse(product_serializer.data,safe=False)
    elif request.method=='POST':
        product_data=JSONParser().parse(request)
        product_serializer=ProductSerializer(data=product_data)
        if product_serializer.is_valid():
            product_serializer.save()
            return JsonResponse("Added Successfully",status=200,safe=False)
        return JsonResponse({"MESAGE" : product_serializer.errors},status=400,safe=False)
    elif request.method=='PUT':
        product_data=JSONParser().parse(request)
        product=Product.objects.get(id=id)
        product_serializer=ProductSerializer(product,data=product_data)
        if product_serializer.is_valid():
            product_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        product=Product.objects.get(id=id)
        product.delete()
        return JsonResponse("Deleted Successfully",safe=False)
    

@csrf_exempt
def userApi(request,id=0):
    if request.method=='GET':
        user = User.objects.all()
        user_serializer=UserSerializer(user,many=True)
        return JsonResponse(user_serializer.data,safe=False)
    elif request.method=='POST':
        user_data=JSONParser().parse(request)
        user_serializer=UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Added Successfully",status=200, safe=False)
        return JsonResponse({"MESAGE" : user_serializer.errors},status=400,safe=False)
    elif request.method=='PUT':
        user_data=JSONParser().parse(request)
        user=User.objects.get(id=id)
        user_serializer=UserSerializer(user,data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        user=User.objects.get(id=id)
        user.delete()
        return JsonResponse("Deleted Successfully",safe=False)