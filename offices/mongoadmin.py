from django.contrib import admin
from .models import Office
from .models import Location
from mongonaut.sites import MongoAdmin

class OfficeAdmin(MongoAdmin):

    def has_view_permission(self, request):
        return True

    def has_edit_permission(self, request):
        return True

    def has_add_permission(self, request):
        return True

    def has_delete_permission(self, request):
        return True

    search_fields = list(('id', 'title'))
    list_fields = list(('id', 'title'))

class LocationAdmin(MongoAdmin):

    def has_view_permission(self, request):
        return True

    def has_edit_permission(self, request):
        return True

    def has_add_permission(self, request):
        return True

    def has_delete_permission(self, request):
        return True

    search_fields = list(('id', 'building'))
    list_fields = list(('id', 'building'))

Office.mongoadmin = OfficeAdmin()
Location.mongoadmin = LocationAdmin()


