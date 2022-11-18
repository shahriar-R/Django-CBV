from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    page_size = 2
    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'total_objects': self.page.paginator.num_pages,
            'results': data
        })