from datetime import datetime

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def index(request):
    date = datetime.now().strftime('%d/%m/%m %H:%M:%S')
    message = 'Clock in the server is live current time is: '
    return Response(data=message + date, status=status.HTTP_200_OK)