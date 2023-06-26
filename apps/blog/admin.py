from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from apps.blog.models import Author, Category

class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category

class CategoryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_filter = ("name", "created_at",)
    list_display = ("name", "created_at",) 
    search_fields = ["name",]
    resource_class = CategoryResource

class AuthorResource(resources.ModelResource):
    class Meta:
        model = Author

class AuthoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_filter = ("name",)
    resource_class = AuthorResource    


admin.site.register(Category, CategoryAdmin)
admin.site.register(Author, AuthoAdmin)
