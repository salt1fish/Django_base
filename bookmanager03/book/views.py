from django.http import HttpResponse, JsonResponse
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


###############查询字符串#####################
"""
查询字符串
http://ip:port/path/path?key1=value1&key2=value2
url 以 ? 分割为两部分
? 前面为 请求路径
? 后边为 查询字符串 查询字符串 类似于字典 key=value 多个数据用 & 拼接
"""


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


def json_res(request):
    # 是HttpResponse的子类
    # JSON --> dict
    # dict --> JSON
    info = {
        "name": "zhy",
        "address": "zg"
    }
    res1 = JsonResponse(data=info)
    ###################################################
    girl_friend = [
        {
            "name": "rose",
            "address": "bj"
        },
        {
            "name": "rose",
            "address": "bj"
        }
    ]
    # In order to allow non-dict objects to be serialized set the safe parameter to False.
    res2 = JsonResponse(data=girl_friend)
    # data 返回的响应数据 一般是字典类型
    """
    safe = True 是表示 我们的data 是字典数据
    JsonResponse 可以把字典转换为json
    safe = False
    现在给了一个非字典数据，出了问题 我们自己负责
    """
    res3 = JsonResponse(data=girl_friend, safe=False)
    return res3


##################Cookie和Session##########################
"""
第一次请求，携带 查询字符串
http://127.0.0.1:8000/set_cookie/?username=zhy&password=123
服务器接收到请求以后，获取username，服务器设置cookie信息，cookie信息包括 username
浏览器接收到服务器的响应后，应该把cookie保存起来

第二次及其之后的请求，我们访问http://127.0.0.1:8000 都会携带cookie信息。服务器就可以
读取cookie信息，来判断用户身份
"""


def set_cookie(request):
    # 1. 获取查询字符串数据
    username = request.GET.get("username")
    password = request.GET.get("password")
    # 2. 服务器设置cookie信息
    # 通过 响应对象.set_cookie 方法
    res = HttpResponse("cookie")
    # key, value = "
    # max_age 是一个秒数 从响应开始计数的一个秒数,默认过期时间是会话结束时（关闭浏览器）
    res.set_cookie("name", username, max_age=60 * 60)
    res.set_cookie("pwd", password)
    # 删除cookie
    res.delete_cookie("name")

    return res


def get_cookie(request):
    # print(request.COOKIES)
    username = request.COOKIES.get("name")
    return HttpResponse(username)


################################
# session 是保存在服务器端 -- 数据相对安全
# session 需要依赖于cookie
"""
第一次请求
http://127.0.0.1:8000/set_session/?username=zhy 我们在访问端设置session信息
服务器同时会生成一个sessionid的cookie信息
浏览器接收到这个信息之后，会把cookie数据保存起来

第二次及其之后的请求 都会携带这个sessionid。服务器会验证这个sessionid。验证没有问题
会读取相关数据。实现业务逻辑
"""


def set_session(request):
    # 1. 模拟 获取用户信息
    username = request.GET.get("username")
    # 2. 设置session信息
    # 假如 我们通过模型查询 查询到了 用户信息
    user_id = 1
    request.session["user_id"] = user_id
    request.session["username"] = username

    # clear 删除session里的数据，但是key有保留
    # request.session.clear()

    # flush 是删除所有的数据，包括key
    # request.session.flush()

    # 如果value是一个整数，session将在value秒没有活动后过期。
    # 如果value为0，那么用户session的Cookie将在用户的浏览器关闭时过期。
    # 如果value为None，那么session有效期将采用系统默认值， 默认为两周，可以通过在settings.py中设置SESSION_COOKIE_AGE来设置全局默认值。
    request.session.set_expiry(60)


    return HttpResponse("set_session")


def get_session(request):
    # user_id = request.session["user_id"]
    # username = request.session["username"]
    # 防止没有匹配到sessionid时报异常
    user_id = request.session.get("user_id")
    username = request.session.get("username")

    content = f"{user_id},{username}"
    return HttpResponse(content)
