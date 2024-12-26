from rest_framework.pagination import PageNumberPagination , CursorPagination

class pagination(CursorPagination):
    page_size = 6
    ordering = 'title'
    cursor_query_param = 'cu'
