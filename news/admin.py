from django.contrib import admin
from news.models import Post, Comment


class CommentInline(admin.TabularInline):
    readonly_fields = ["author", "body", "pub_date"]
    model = Comment
    extra = 0

    def has_add_permission(self, request):
        return False


class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "pub_date", "has_image", "comment_count"]
    list_filter = ["author"]
    readonly_fields = ["pub_date"]
    inlines = (CommentInline, )

    def comment_count(self, instance):
        return instance.comment_set.count()

admin.site.register(Post, PostAdmin)
