from django.http import HttpResponse
from django.shortcuts import render
from book.models import BookInfo


# Create your views here.
def create_book(request):
    BookInfo.objects.create(
        name='abc',
        pub_date='2000-1-1',
        readcount=10
    )
    return HttpResponse("ok")


# 接收路径中的参数，参数名称不能错，参数位置可以改变
def shop(request, shop_id, city_id):
    return HttpResponse(f"城市id：{city_id} 商店id：{shop_id}")
