from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import FileSerializer
from .bapCleanAndTokenize import cleanAndTokenize, cleanAndTokenizev2
from .models import File
from django.http import JsonResponse


class UploadFile(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():

            file_serializer.save()
            data = cleanAndTokenize(request.data['file'])
            # return Response(file_serializer.data, status=status.HTTP_201_CREATED)

            return Response(data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CleanWithParameters(APIView):

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        uuid = request.data['uuid']
        file = File.objects.all().filter(uuid=uuid)
        # guid = request.data['guid']
        data = cleanAndTokenizev2(file)

        return Response({"message": "success", "data": data})
