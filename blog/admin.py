from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe
from django_ckeditor_5.widgets import CKEditor5Widget

from .models import *

# Register your models here.

# class CommentForm(forms.ModelForm):
#     """Form for comments to the article."""
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields["text"].required = False
#
#     class Meta:
#         model = Comment
#         fields = ("author", "text")
#         widgets = {
#             "text": CKEditor5Widget(
#                 attrs={"class": "django_ckeditor_5"}, config_name="comment"
#             )
#         }


class PostAdminForm(forms.ModelForm):
    """Form for comments to the article."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["content"].required = False

    class Meta:
        model = Post
        fields = ('content',)
        widgets = {
            "text": CKEditor5Widget(
                attrs={"class": "django_ckeditor_5"}, config_name="post"
            )
        }


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    forms = PostAdminForm
    list_display = ('pk', 'title', 'created_at', 'category', 'get_photo', 'views', )
    list_display_links = ('pk', 'title', )
    search_fields = ('title', )
    list_filter = ('category', 'tags', )
    save_on_top = True
    readonly_fields = ('views', 'created_at', 'get_photo')
    fields = ('title', 'slug', 'author', 'content', 'photo', 'get_photo', 'category', 'tags', 'created_at', 'views')


    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50">')
        else:
            return 'none photo'

    get_photo.short_description = 'Photo'


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)

