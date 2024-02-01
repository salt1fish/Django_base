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
    query_params = request.GET
    print(query_params)
    # order = query_params['order']
    # order = query_params.get('order')
    # print(order)

    # http://127.0.0.1:8000/123/125/?order=readcount
    # http://127.0.0.1:8000/123/125/?order=readcount&order=commentcount
    # <QueryDict: {'order': ['readcount']}>
    # QueryDict 具有字典的特性
    # 还具有 一键多值
    # <QueryDict: {'order': ['readcount', 'commentcount']}>
    # 多值时 get 和 关键字 只能得到最后一个值
    # order = query_params.get('order')
    # order = query_params['order']
    # 可以得到一个列表
    order = query_params.getlist('order')
    print(order)

    content = f"城市id：{city_id}---商店id：{shop_id}---query_params：{order}"
    return HttpResponse(content)


def register(request):
    data_post = request.POST
    print(data_post)
    return HttpResponse("ok")


def json(request):
    # request.POST json数据不能通过 request.POST获取数据
    body = request.body
    # b'{\r\n    "name": "zhy",\r\n    "age": 18\r\n}'
    # print(body)
    body_str = body.decode()
    """
    {
        "name": "zhy",
        "age": 18
    }
    """
    print(body_str)
    # <class 'str'>
    print(type(body_str))
    # json形式的字符串 可以转换为 python的字典
    import json
    body_dict = json.loads(body_str)
    print(body_dict)

    ###########请求头############
    # 可以通过request.META属性获取请求头headers中的数据，request.META为字典类型
    print(request.META)

    return HttpResponse("json")

###############查询字符串#####################
"""
查询字符串
http://ip:port/path/path?key1=value1&key2=value2
url 以 ? 分割为两部分
? 前面为 请求路径
? 后边为 查询字符串 查询字符串 类似于字典 key=value 多个数据用 & 拼接
"""
