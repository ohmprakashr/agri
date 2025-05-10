from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import CropProduct  
from .serializers import CropProductSerializer 

@api_view(['GET', 'POST'])
def crop_product_list_create(request):
    if request.method == 'GET':
        crops = CropProduct.objects.all().order_by('-created_at')
        serializer = CropProductSerializer(crops, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = CropProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
