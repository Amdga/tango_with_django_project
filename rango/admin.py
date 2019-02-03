from django.contrib import admin
from rango.models import Category, Page


# Admin site customisation
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')
    pass


# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)



