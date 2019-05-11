from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import FileSerializer
from .models import File

from .bapCleanAndTokenize import cleanAndTokenize


class UploadFile(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():
            print(file_serializer)
            file_serializer.save()
            data = cleanAndTokenize(request.data['file'])
            #return Response(file_serializer.data, status=status.HTTP_201_CREATED)

            return Response(data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CleanWithParameters(APIView):

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        # file = File.objects.all().filter('uuid')
        # guid = request.data['guid']

        return Response({"message": "sdg"})
