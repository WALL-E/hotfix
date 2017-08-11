from .models import Category, System, App, Version, Patch, Release
from rest_framework import viewsets
from .serializers import CategorySerializer, SystemSerializer, AppSerializer
from .serializers import VersionSerializer, PatchSerializer, ReleaseSerializer
from rest_framework import filters


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SystemViewSet(viewsets.ModelViewSet):
    queryset = System.objects.all()
    serializer_class = SystemSerializer


class AppViewSet(viewsets.ModelViewSet):
    queryset = App.objects.all()
    serializer_class = AppSerializer
    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter)
    filter_fields = ('category_id', 'system_id')
    ordering_fields = ('id', 'name')


class VersionViewSet(viewsets.ModelViewSet):
    queryset = Version.objects.all()
    serializer_class = VersionSerializer
    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter)
    filter_fields = ('app_id',)
    ordering_fields = ('id', 'name', 'create_time')


class PatchViewSet(viewsets.ModelViewSet):
    queryset = Patch.objects.all()
    serializer_class = PatchSerializer
    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter)
    filter_fields = ('version_id',)
    ordering_fields = ('id', 'size', 'upload_time')


class ReleaseViewSet(viewsets.ModelViewSet):
    queryset = Release.objects.all()
    serializer_class = ReleaseSerializer
    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter)
    filter_fields = ('patch_id',)
    ordering_fields = ('id', 'serial_number', 'create_time', 'update_time')
