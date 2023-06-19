from rest_framework.pagination import PageNumberPagination

class WatchListPagination(PageNumberPagination):
    page_size=5
    # last_page_strings= 'last'