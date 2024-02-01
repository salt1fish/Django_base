from django.urls import path
from book.views import create_book, shop, register, json, method

urlpatterns = [
    path('create/', create_book),
    # 获取请求路径中的参数
    path('<city_id>/<shop_id>/', shop),
    path('register/', register),
    path('json/', json),
    path('method/', method),
]
