from django.urls import path
from book.views import create_book, shop, register, json, method, response, json_res
from django.urls import converters
from django.urls import register_converter


# 1. 定义转换器
class MobileConverter:
    regex = '1[3-9]\d{9}'

    # 验证没有问题的数据，给视图函数
    def to_python(self, value):
        return int(value)

    # # 将匹配结果用于反向解析传值时使用（了解）
    # def to_url(self, value):
    #     return str(value)


# 2. 先注册转换器，才能在第三步中使用
# converter 转换器类
# type_name 转换器名字
register_converter(MobileConverter, 'phone')

urlpatterns = [
    path('create/', create_book),
    # 获取请求路径中的参数
    # path('<city_id>/<shop_id>/', shop),
    # <转换器名字：变量名>
    # 转换器会对变量数据进行 正则的验证
    path('<int:city_id>/<phone:shop_id>/', shop),
    path('register/', register),
    path('json/', json),
    path('method/', method),
    path('res/', response),
    path('json_res/', json_res),
]
"""
    from django.urls import converters

    class IntConverter:
        regex = '[0-9]+'

        def to_python(self, value):
            return int(value)

        def to_url(self, value):
            return str(value)
"""
