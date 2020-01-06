from django.shortcuts import render
from django.http import HttpResponse

# 首页
from blog.models import Category, Banner, Article, Tag, Link


def index(request):
    allcategory = Category.objects.all()
    banner = Banner.objects.filter(is_active=True)[0:4]
    tui = Article.objects.filter(tui__id=1)[:3]
    allarticle = Article.objects.all().order_by('-id')[0:10]
    hot = Article.objects.all().order_by('views')[:10]
    remen = Article.objects.filter(tui__id=2)[:6]
    tags = Tag.objects.all()
    links = Link.objects.all()
    context = {'allcategory': allcategory, 'banner': banner, 'tui': tui, 'allarticle': allarticle, 'hot': hot,
               'remen': remen, 'tags': tags, 'links': links}
    return render(request, 'index.html', context)


# 列表页
def list(request, lid):
    pass


# 内容页
def show(request, sid):
    pass


# 标签页
def tag(request, tag):
    pass


# 搜索页
def search(request):
    pass


# 关于我们
def about(request):
    pass
