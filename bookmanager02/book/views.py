from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse("index")


#################增加数据#########################
from book.models import BookInfo

# 方式1
book = BookInfo(name="django",
                pub_date="2000-1-1",
                read_count=10)
# 必须调用 对象的save方法才能将数据保存到数据库
book.save()

# 方式2
# objects -- 相当于一个代理 实现增删改查
BookInfo.objects.create(name="测试开发",
                        pub_date="2020-1-1",
                        read_count=100)

#################修改数据#########################
# 方式1
# select * from bookinfo where id=6
BookInfo.objects.get(id=10)

book.name = "运维开发入门"
# 想要保存数据 需要调用 对象的save方法
book.save()

# 方式2
# filter 过滤
BookInfo.objects.filter(id=10).update(name="爬虫入门", comment_count=666)

# 错误的 get() 方法返回的对象没有update方法
# BookInfo.objects.get(id=10).update(name="555", comment_count=999)


#################删除数据#########################
# 方式1
book = BookInfo.objects.get(id=10)
# 删除分两种：物理删除（这条记录的数据 删除） 和 逻辑删除 （修改标记位 例如 is_delete=False）
book.delete()

# 方式2
BookInfo.objects.get(id=10).delete()
BookInfo.objects.filter(id=4).delete()

#################查询数据#########################
# get 查询单一结果，如果不存在会抛出模型类 DoesNotExist异常
try:
    book = BookInfo.objects.get(id=1)
except BookInfo.DoesNotExist:
    print("查询结果不存在")
# all查询多个结果
books = BookInfo.objects.all()
from book.models import PeopleInfo

PeopleInfo.objects.all()
# count查询结果数量
BookInfo.objects.all().count()
BookInfo.objects.count()

#################过滤数据#########################
# 实现SQL中的where功能 包括
# filter 过滤出多个结果
# exclude 排除掉符合条件剩下的结果
# get 过滤单一结果

# 模型类名.objects.filter(属性名__运算符=值)       获取n个结果 n=0,1,2……
# 模型类名.objects.exclude(属性名__运算符=值)      获取n个结果 n=0,1,2……
# 模型类名.objects.get(属性名__运算符=值)          获取1个结果 或者 异常
"""
查询编号为1的图书
查询书名包含'湖'的图书
查询书名以'部'结尾的图书
查询书名为空的图书
查询编号为1或3或5的图书
查询编号大于3的图书
查询1980年发表的图书
查询1990年1月1日后发表的图书
"""
# 查询编号为1的图书
BookInfo.objects.get(id=1)  # 简写形式 （属性名=值）
BookInfo.objects.get(id__exact=1)  # 完整形式 （id_exact=值）
BookInfo.objects.get(pk=1)  # pk primary key 主键

# get得到的是一个 对象
BookInfo.objects.get(id=1)  # <BookInfo: 射雕英雄传>
# filter得到的是 列表
BookInfo.objects.filter(id=1)  # <QuerySet [<BookInfo: 射雕英雄传>]>

# 查询书名包含'湖'的图书
BookInfo.objects.filter(name__contains="湖")

# 查询书名以'部'结尾的图书
BookInfo.objects.filter(name__endswith="部")

# 查询书名为空的图书
BookInfo.objects.filter(name__isnull=True)

# 查询编号为1或3或5的图书
BookInfo.objects.filter(id__in=[1, 3, 5])

# 查询编号大于3的图书
# 大于 gt
# 大于等于 gte
# 小于 lt
# 小于等于 lte
BookInfo.objects.filter(id__gte=3)

# 查询编号不等于3的图书
BookInfo.objects.exclude(id=3)

# 查询1980年发表的图书
BookInfo.objects.filter(pub_date__year=1980)

# 查询1990年1月1日后发表的图书
BookInfo.objects.filter(pub_date__gt="1990-1-1")

##################################################
from django.db.models import F
# 用处： 两个属性的比较
# 语法形式： 以filter为例 模型类名.objects.filter(属性名__运算符=('第二个属性名'))
# 查询阅读量大于等于评论量的图书
BookInfo.objects.filter(read_count__gte=F('comment_count'))

##################################################
# 并且查询
# 查询阅读量大于20，并且编号小于3的图书。

BookInfo.objects.filter(read_count__gt=20).filter(id__lt=3)
BookInfo.objects.filter(read_count__gt=20, id__lt=3)

# 或者查询
# 查询阅读量大于20，或编号小于3的图书
from django.db.models import Q
# 并且语法：模型类名.objects.filter(Q(属性名__运算符=值) & Q(属性名__运算符=值)&……)
# 或者语法：模型类名.objects.filter(Q(属性名__运算符=值) | Q(属性名__运算符=值)|……)
BookInfo.objects.filter(Q(read_count__gt=20) | Q(id__lt=3))

# not 非 语法：模型类名.objects.filter(~Q(属性名__运算符=值))
# 查询编号不等于3的图书
BookInfo.objects.filter(~Q(id__exact=3))
