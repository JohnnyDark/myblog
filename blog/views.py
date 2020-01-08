import paginator as paginator
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.http import HttpResponse

# 首页
from blog.models import Category, Banner, Article, Tag, Link


def index(request):
    allcategory = Category.objects.all()  # 文章类型
    banner = Banner.objects.filter(is_active=True)[0:4]  # 轮播图
    tui = Article.objects.filter(tui__id=1)[:3]  # id=1推荐阅读的文章
    allarticle = Article.objects.all().order_by('-id')[0:10]  # 最新文章
    hot = Article.objects.all().order_by('views')[:10]  # 热门文章排行
    remen = Article.objects.filter(tui__id=2)[:6]  # 热门推荐文章
    tags = Tag.objects.all()  # 所有标签
    links = Link.objects.all()  # 友情链接
    context = {'allcategory': allcategory, 'banner': banner, 'tui': tui, 'allarticle': allarticle, 'hot': hot,
               'remen': remen, 'tags': tags, 'links': links}
    return render(request, 'index.html', context)


# 列表页
def list(request, lid):
    list = Article.objects.filter(category_id__id=lid)
    cname = Category.objects.get(id=lid)
    remen = Article.objects.filter(tui__id=2)[:6]
    allcategory = Category.objects.all()
    tags = Tag.objects.all()
    # 分页操作
    page = request.GET.get('page')  # url中获取当前页码
    paginator = Paginator(list, 2)  # 对查询到的数据进行分页，一页显示5条
    try:
        list = paginator.page(page)  # 获取当前页码的数据
    except PageNotAnInteger:
        list = paginator.page(1)  # 如果用户输入的页码不是整数，显示第一页
    except EmptyPage:
        list = paginator.page(paginator.num_pages)  # 如果输入的页码不在页码列表中，显示最后一页
    return render(request, 'list.html', locals())


# 内容页
def show(request, sid):
    article = Article.objects.get(id=sid)
    allcategory = Category.objects.all()
    tags = Tag.objects.all()
    remen = Article.objects.filter(tui__id=2)[:6]
    hot = Article.objects.all().order_by("?")[:10] # 您可能感兴趣
    previous_blog = Article.objects.filter(created_time__gt=article.created_time, category=article.category.id).first()
    next_blog = Article.objects.filter(created_time__lt=article.created_time, category=article.category.id).last()
    article.views = article.views+1
    article.save()
    return render(request, 'show.html', locals())


# 标签页
def tag(request, tag):
    list = Article.objects.filter(tags__name=tag)
    tname = Tag.objects.get(name=tag)
    remen = Article.objects.filter(tui__id=2)[:6]
    allcategory = Category.objects.all()
    tags = Tag.objects.all()
    # 分页操作
    page = request.GET.get('page')  # url中获取当前页码
    paginator = Paginator(list, 2)  # 对查询到的数据进行分页，一页显示5条
    try:
        list = paginator.page(page)  # 获取当前页码的数据
    except PageNotAnInteger:
        list = paginator.page(1)  # 如果用户输入的页码不是整数，显示第一页
    except EmptyPage:
        list = paginator.page(paginator.num_pages)  # 如果输入的页码不在页码列表中，显示最后一页
    return render(request, 'tags.html', locals())

# 搜索页
def search(request):
    ss = request.GET.get('search')
    list = Article.objects.filter(title__icontains=ss)
    remen = Article.objects.filter(tui__id=2)[:6]
    allcategory = Category.objects.all()
    tags = Tag.objects.all()
    # 分页操作
    page = request.GET.get('page')  # url中获取当前页码
    paginator = Paginator(list, 2)  # 对查询到的数据进行分页，一页显示5条
    try:
        list = paginator.page(page)  # 获取当前页码的数据
    except PageNotAnInteger:
        list = paginator.page(1)  # 如果用户输入的页码不是整数，显示第一页
    except EmptyPage:
        list = paginator.page(paginator.num_pages)  # 如果输入的页码不在页码列表中，显示最后一页
    return render(request, 'search.html', locals())


# 关于我们
def about(request):
    allcategory = Category.objects.all()
    return render(request, 'page.html', locals())
