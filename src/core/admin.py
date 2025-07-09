from django.contrib import admin

from core.models import ContentType, Group


class ContentTypeAdmin(admin.ModelAdmin):
    list_display = ("key", "name", "name_plural")
    search_fields = ("name", "name_plural")
    ordering = ("name",)


admin.site.register(Group)
admin.site.register(ContentType, ContentTypeAdmin)
