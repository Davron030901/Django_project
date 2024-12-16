from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Item
from api.serializers import ItemSerializer

@api_view(['GET'])
def getData(request):
    items=Item.objects.all()
    serializer=ItemSerializer(items,many=True)
    person=serializer.data 
    # person={'name':'Dennis','age':25}
    return Response(person)

@api_view(['POST'])
def addItem(request):
    serializer=ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)