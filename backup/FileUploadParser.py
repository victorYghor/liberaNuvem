from cgi import parse_header
from lib2to3.pgen2.parse import ParseError

from django.core.files.uploadhandler import StopFutureHandlers
from django.http import HttpResponse
from django.http.multipartparser import ChunkIter
from rest_framework import views, status
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser, DataAndFiles, BaseParser
from rest_framework.response import Response

from liberaNuvem import settings

class FileUploadParser(BaseParser):
    """
    Parser for file upload data.
    """
    media_type = "*/*"

    def parse(self, stream, media_type=None, parser_context=None):
        """
        Treats the incoming bytestream as a raw file upload and returns
        a `DateAndFiles` object.

        `.data` will be None (we expect request body to be a file content).
        `.files` will be a `QueryDict` containing one "file" element.
        """

        parser_context = parser_context or {}
        request = parser_context["request"]
        encoding = parser_context.get("encoding", settings.DEFAULT_CHARSET)
        meta = request.META
        upload_handlers = request.upload_handlers
        filename = self.get_filename(stream, media_type, parser_context)

        # Note that this code is extracted from Django's handling of
        # file uploads in MultiPartParser.
        content_type = meta.get("HTTP_CONTENT_TYPE",
                                meta.get("CONTENT_TYPE", ""))
        try:
            content_length = int(meta.get("HTTP_CONTENT_LENGTH",
                                          meta.get("CONTENT_LENGTH", 0)))
        except (ValueError, TypeError):
            content_length = None

        # See if the handler will want to take care of the parsing.
        for handler in upload_handlers:
            result = handler.handle_raw_input(None,
                                              meta,
                                              content_length,
                                              None,
                                              encoding)
            if result is not None:
                return DataAndFiles(None, {"file": result[1]})

        # This is the standard case.
        possible_sizes = [x.chunk_size for x in upload_handlers if x.chunk_size]
        chunk_size = min([2 ** 31 - 4] + possible_sizes)
        chunks = ChunkIter(stream, chunk_size)
        counters = [0] * len(upload_handlers)

        for handler in upload_handlers:
            try:
                handler.new_file(None, filename, content_type,
                                 content_length, encoding)
            except StopFutureHandlers:
                break

        for chunk in chunks:
            for i, handler in enumerate(upload_handlers):
                chunk_length = len(chunk)
                chunk = handler.receive_data_chunk(chunk, counters[i])
                counters[i] += chunk_length
                if chunk is None:
                    break

        for i, handler in enumerate(upload_handlers):
            file_obj = handler.file_complete(counters[i])
            if file_obj:
                return DataAndFiles(None, {"file": file_obj})
        raise ParseError("FileUpload parse error - "
                         "none of upload handlers can handle the stream")

    def get_filename(self, stream, media_type, parser_context):
        """
        Detects the uploaded file name. First searches a "filename" url kwarg.
        Then tries to parse Content-Disposition header.
        """
        try:
            return parser_context["kwargs"]["filename"]
        except KeyError:
            pass

        try:
            meta = parser_context["request"].META
            disposition = parse_header(meta["HTTP_CONTENT_DISPOSITION"])
            return disposition[1]["filename"]
        except (AttributeError, KeyError):
            pass
