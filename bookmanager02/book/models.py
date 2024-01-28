from django.db import models

"""
1. 模型类 需要继承 models.Model
2. 定义属性
    id 系统会默认生成
    2.1 属性名=models.类型（选项）
        不要使用python，mysql关键字
        不要使用连续的下划线（__）
    2.2 类型 MySQL的类型
    2.3 选项 是否有默认值，是否唯一，是否为null
        CharFiled必须设置max_length
        verbose_name 主要是 admin站点使用
3. 改变表的名称
    默认表的名称是：子应用_类名 都是小写
    修改表的名字
"""


# Create your models here.
class BookInfo(models.Model):
    name = models.CharField(max_length=10, unique=True, verbose_name="名字")
    pub_date = models.DateField(null=True)
    read_count = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "bookinfo"  # 修改表的名字
        verbose_name = "书籍管理"  # admin站点使用的（了解）


class PeopleInfo(models.Model):
    # 定义一个有序字典
    GENDER_CHOICE = (
        (1, 'male'),
        (2, 'female')
    )

    name = models.CharField(max_length=10, unique=True)
    gender = models.SmallIntegerField(choices=GENDER_CHOICE, default=1)
    description = models.CharField(max_length=100, null=True)
    is_delete = models.BooleanField(default=False)

    # 外键
    # 系统会自动为外键添加_id

    # 外键的级联操作
    # 主表 和 从表
    # 1 对 多
    # 书籍 对 人物
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "peopleinfo"

