from ..models import Review
from ..serializers import ReviewSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

class ReviewList(APIView):
    """
    List all reviews
    """
    def get(self, request, format=None):
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        if request.data.get('user') != request.user.id:
            return Response(status=status.HTTP_403_FORBIDDEN)
        
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
class ReviewDetails(APIView):
    def get(self, request, pk, format=None):
        try:
            review = Review.objects.get(pk=pk)
            serializer = ReviewSerializer(review)
            return Response(serializer.data)
        except Review.DoesNotExist:
            raise Http404
        
    def put(self, request, pk, format=None):
        if Review.objects.get(pk=pk).user.id != request.user.id:
            return Response(status=status.HTTP_403_FORBIDDEN)
        
        review = Review.objects.get(pk=pk)
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        if Review.objects.get(pk=pk).user.id != request.user.id:
            return Response(status=status.HTTP_403_FORBIDDEN)
        
        review = Review.objects.get(pk=pk)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    