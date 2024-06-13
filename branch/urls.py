from django.urls import path
from .views import BranchListCreateView, BranchDetailView,ReviewListCreate,ReviewDetail

urlpatterns = [
    path('branches/', BranchListCreateView.as_view(),name='branch-list-create'),
    path('branches/<int:pk>/', BranchDetailView.as_view(), name='branch-detail'),
    path('reviews/', ReviewListCreate.as_view(), name='review-list-create'),
    path('reviews/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),
    

]