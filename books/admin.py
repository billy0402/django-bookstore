from django.contrib import admin

from .models import Book


# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'upper_case_name', 'price']
    search_fields = ['name']
    list_filter = ['name', 'price']

    def upper_case_name(self, obj):
        return obj.name.upper()
    upper_case_name.short_description = 'upper_case_name'


# admin.site.register(Book, BookAdmin)
