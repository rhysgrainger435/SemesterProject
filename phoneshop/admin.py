from django.contrib import admin
from .models import Category,Product,Comment

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}

admin.site.register(Category,CategoryAdmin)

class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price' ,'description', 'category', 'stock','available', 'created', 'updated', 'slug']
    list_editable = ['price','stock','available']
    list_per_page = 20
    prepopulated_fields = {'slug': ('name', )}
    inlines = [
        CommentInline
    ]
admin.site.register(Product,ProductAdmin)



admin.site.register(Comment)


