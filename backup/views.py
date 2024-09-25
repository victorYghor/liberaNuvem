import os
from cgi import parse_header
from lib2to3.pgen2.parse import ParseError

from django.core.files.uploadhandler import StopFutureHandlers
from django.http import HttpResponse
from django.http.multipartparser import ChunkIter
from rest_framework import views, status
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from liberaNuvem import settings
import boto3

class FileUploadView(views.APIView):
    parser_classes = (FileUploadParser, )
    media_type = "*/*"
    def post(self, request, *args, **kwargs):
        if request.headers['api-key'] != os.environ['API_KEY']:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        if 'file' not in request.FILES:
            return Response({'detail': 'No file provided'}, status=status.HTTP_400_BAD_REQUEST)

        file_uploaded = request.FILES['file']
        s3 = boto3.resource('s3')
        s3.Bucket('liberanuvem').put_object(Key='backup.zip', Body=file_uploaded)

        # Aqui você pode fazer algo com o arquivo recebido
        return Response(status=status.HTTP_204_NO_CONTENT)

