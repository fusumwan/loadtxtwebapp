class MediaType:
    """
    A class to represent HTTP Media Types.
    This version includes a subset of functionality focusing on media type constants
    and simple parsing.
    """

    # Constants for commonly used media types
    ALL = "*/*"
    APPLICATION_ATOM_XML = "application/atom+xml"
    APPLICATION_CBOR = "application/cbor"
    APPLICATION_FORM_URLENCODED = "application/x-www-form-urlencoded"
    APPLICATION_GRAPHQL = "application/graphql+json"
    APPLICATION_JSON = "application/json"
    APPLICATION_JSON_UTF8 = "application/json;charset=UTF-8"  # Deprecated
    APPLICATION_OCTET_STREAM = "application/octet-stream"
    APPLICATION_PDF = "application/pdf"
    APPLICATION_PROBLEM_JSON = "application/problem+json"
    APPLICATION_PROBLEM_JSON_UTF8 = "application/problem+json;charset=UTF-8"  # Deprecated
    APPLICATION_PROBLEM_XML = "application/problem+xml"
    APPLICATION_RSS_XML = "application/rss+xml"
    APPLICATION_XHTML_XML = "application/xhtml+xml"
    APPLICATION_XML = "application/xml"
    IMAGE_GIF = "image/gif"
    IMAGE_JPEG = "image/jpeg"
    IMAGE_PNG = "image/png"
    MULTIPART_FORM_DATA = "multipart/form-data"
    MULTIPART_FORM_DATA_VALUE = "multipart/form-data"
    MULTIPART_MIXED_VALUE = "multipart/mixed"
    MULTIPART_RELATED_VALUE = "multipart/related"
    TEXT_HTML = "text/html"
    TEXT_MARKDOWN = "text/markdown"
    TEXT_PLAIN = "text/plain"
    TEXT_XML = "text/xml"
    # Add other constants as necessary

    @staticmethod
    def parse(media_type_str):
        """
        Parses a string into a MediaType object. This simplistic implementation
        splits the type and subtype, and does not fully parse parameters.
        """
        parts = media_type_str.split(";")
        main_type, subtype = parts[0].split("/")
        parameters = {}
        for part in parts[1:]:
            if "=" in part:
                key, value = part.split("=")
                parameters[key.strip()] = value.strip()
        return MediaType(main_type.strip(), subtype.strip(), parameters)

    def __init__(self, type, subtype, parameters=None):
        self.type = type
        self.subtype = subtype
        self.parameters = parameters if parameters is not None else {}

    def __str__(self):
        """
        Returns the string representation of the media type.
        """
        params = "; ".join([f'{k}={v}' for k, v in self.parameters.items()])
        return f"{self.type}/{self.subtype}; {params}" if self.parameters else f"{self.type}/{self.subtype}"

