from django.shortcuts import render

from api.models.productfilter import ProductFilter
from ..models.product import *
from ..serializers import *
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from silk.profiling.profiler import silk_profile
#views from product
class ListAllProduct(GenericAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    @silk_profile(name='Product List')
    def get(self, request, *args, **kwargs):
        products=self.get_queryset()
        serializer=self.get_serializer(products, many=True)
        return Response ({"success":True, "message":"Products Retrieved", "data":serializer.data})

class ListProduct(GenericAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    def get(self, request, *args, **kwargs):
        product=self.get_object()
        serializer=self.get_serializer(product)
        return Response ({"success":True, "message":"Single Product Retrieved", "data":serializer.data})

class CreateProduct(GenericAPIView):
    # queryset=Product.objects.all()
    # serializer_class=ProductSerializer
    def post(self, request, *args, **kwargs):
        serializer=ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"success":True, "message":"Created", "data":serializer.data})
        return Response ({"success":False, "message":"Not Created"})

class DeleteProduct(GenericAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    def delete(self, request, *args, **kwargs):
        product=self.get_object() #problem case: two different tables call issue. so below logic is used
        product.delete()
        return Response({"Status":"Deleted"})
    def put(self, request, *args, **kwargs):
        product=self.get_queryset().filter(id=kwargs.get("pk")).first()
        #  product=Product.objects.filter(id=kwargs.get("pk")).first() #more usable for gettingo object
        serializer=ProductSerializer(product, request.data)
        if serializer.is_valid():
             serializer.save()
             return Response({"Status":"Succes","Data":serializer.data})
        return Response({"Status":"Update Error"})
    
class ProductSearch(GenericAPIView): #searching without django-filter framework
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    def get(self, request, search, *args, **kwargs):
        products=self.get_queryset().filter(name__icontains=search)
        serializer=self.get_serializer(products, many=True)
        return Response({"Status":"Success","Data":serializer.data})


   

    



