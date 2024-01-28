from django.urls import path
from book.views import create_book, shop

urlpatterns = [
    path('create/', create_book),
    # 获取请求路径中的参数
    path('<city_id>/<shop_id>/', shop),
]