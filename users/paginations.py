from rest_framework import pagination
from rest_framework.response import Response


class CustomPagination(pagination.PageNumberPagination):
    page_size = 5
    page_size_query_param = "limit"
    max_page_size = 500
    page_query_param = "page"
