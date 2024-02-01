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


def method(request):
    """
    method：一个字符串，表示请求使用的HTTP方法，常用值包括：'GET'、'POST'。
    user：请求的用户对象。
    path：一个字符串，表示请求的页面的完整路径，不包含域名和参数部分。
    encoding：一个字符串，表示提交的数据的编码方式。
            如果为None则表示使用浏览器的默认设置，一般为utf-8。
            这个属性是可写的，可以通过修改它来修改访问表单数据使用的编码，接下来对属性的任何访问将使用新的encoding值。
    FILES：一个类似于字典的对象，包含所有的上传文件。
    :param request:
    :return:
    """
    # 一个字符串，表示请求使用的HTTP方法，常用值包括：'GET'、'POST'
    print(request.method)
    return HttpResponse("method")


def response(request):
    # HTTP status code must be an integer from 100 to 599.
    # return HttpResponse("res", status=666)
    # 1xx
    # 2xx
    #   200 成功
    # 3xx
    # 4xx 请求有问题
    #   404 找不到页面 路由有问题
    #   403 禁止访问 权限问题
    # 5xx 服务器错误
    # 可以使用django.http.HttpResponse来构造响应对象。
    # HttpResponse(content=响应体, content_type=响应体数据类型, status=状态码)
    res = HttpResponse("res", status=200)
    # 也可通过HttpResponse对象属性来设置响应体、响应体数据类型、状态码：
    #   content：表示返回的内容。
    #   status_code：返回的HTTP响应状态码。
    res.status_code = 300
    # 响应头可以直接将HttpResponse对象当做字典进行响应头键值对的设置：
    res["name"] = "zhy"

    return res


###############查询字符串#####################
"""
查询字符串
http://ip:port/path/path?key1=value1&key2=value2
url 以 ? 分割为两部分
? 前面为 请求路径
? 后边为 查询字符串 查询字符串 类似于字典 key=value 多个数据用 & 拼接
"""
