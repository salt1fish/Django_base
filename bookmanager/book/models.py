from django.db import models

"""
1. 自己的模型类 需要继承自 models.Model
2. 系统会自动为我们添加一个主键 --id
3. 字段
    字段名 = ，models.类型（选项）
    字段名就是数据库表的字段名
    字段名不要使用python，mysql等关键字
    
    char（M）
    varchar（M）
    M 就是选项
"""


# Create your models here.
# 准备书籍列表信息的模型类
class BookInfo(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


# 准备人物列表信息的模型类
class PeopleInfo(models.Model):
    name = models.CharField(max_length=10)
    gender = models.BooleanField()
    # 外键约束：人物属于哪本书
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)
