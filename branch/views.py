
from rest_framework import generics
from branch.serializers import BranchSerializer, ReviewSerializer
from branch.models import Branch,Review
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

# Create your views here.


class BranchListCreateView(generics.ListCreateAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    
    def delete(self, request, pk= None):
        pk = request.data.get('id')
        Branches = get_object_or_404(Branch, pk=pk)
        Branches.delete()
        return Response({ 'message':'Branch deleted successfully'})
            
        
# class BranchDeleteView(generics.ListCreateAPIView):
#     def delete(self, request):
#         product_id = request.data.get('id')
#         if not product_id:
#             return Response({'error': 'Product ID is required'})
        
#         product = get_object_or_404(product, pk=product_id)
#         product.delete()
#         return Response({'message': 'Product deleted successfully'})  

class BranchDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    


class ReviewListCreate(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer



class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
