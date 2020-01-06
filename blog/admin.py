from django.contrib import admin

from .models import Article, Tag, Category, Link, Banner, Tui


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    # 文章列表里想要显示的字段
    list_display = ['id', 'category', 'title', 'tui', 'user', 'views', 'created_time']
    # 每页显示的数据量
    list_per_page = 50
    # 后台数据列表排序方式, 元组类型
    ordering = ('-created_time',)
    # 设置那些字段可以进入编辑页面
    list_display_links = ('id', 'title')


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ['id', 'text_info', 'img', 'link_url', 'is_active']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'index']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Tui)
class TuiAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'link_url']
