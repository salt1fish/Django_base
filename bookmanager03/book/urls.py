from django.urls import path
from book.views import create_book, shop, register, json, method
from django.urls import converters

urlpatterns = [
    path('create/', create_book),
    # 获取请求路径中的参数
    # path('<city_id>/<shop_id>/', shop),
    # <转换器名字：变量名>
    # 转换器会对变量数据进行 正则的验证
    path('<int:city_id>/<shop_id>/', shop),
    path('register/', register),
    path('json/', json),
    path('method/', method),
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