
from product.serializers import ProductSerializer
from rest_framework import viewsets
from product.models import product
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

class ProductViewSet(viewsets.ModelViewSet):
    queryset = product.objects.all()
    serializer_class = ProductSerializer
    
    
    def delete(self, request, pk= None):
        pk = request.data.get('id')
        Branches = get_object_or_404(product, pk=pk)
        Branches.delete()
        return Response({ 'message':'Product deleted successfully'})
        
    
    

    

