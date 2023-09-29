from rest_framework.pagination import PageNumberPagination

class BoothPagination(PageNumberPagination):
    page_size = 10