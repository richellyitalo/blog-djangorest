from rest_framework import viewsets, pagination
from rest_framework.response import Response
from rest_framework.decorators import action

from core.models import Post, Page, Banner
from core.serializers import (
    PostSerializer,
    PageSerializer,
    BannerSerializer
)
from core.viewsets import PublicViewSet, PublicViewSetNoPagination


class PostViewSet(PublicViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'

    def retrieve(self, request, slug=None):
        post = self.get_object()
        serializer = self.get_serializer(post)
        post.add_view()
        return Response(serializer.data)

    @action(detail=False, methods=['GET'])
    def most_vieweds(self, request):
        queryset = self.paginate_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return self.get_paginated_response(serializer.data)


class PageViewSet(PublicViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    lookup_field = 'slug'


class BannerViewSet(PublicViewSetNoPagination):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer

    def get_queryset(self):
        queryset = Banner.objects.order_by('sort_order')
        return queryset

    def retrieve(self, request, pk=None):
        banner = self.get_object()
        serializer = self.get_serializer(banner)
        banner.add_click()
        return Response(serializer.data)
