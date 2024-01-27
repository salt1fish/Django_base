from django.shortcuts import render
from django.http import HttpResponse

"""
视图
所谓视图，就是python函数
视图函数有两个要求：
    1. 视图函数的第一个参数就是接收请求。这个请求就是 HttpRequest 的类对象
    2. 必须返回一个响应
"""


# Create your views here.
def index(request):
    # return HttpResponse("ok")

    # 参数 request, template_name, context=None
    # request 请求
    # template_name 模板名字
    # context=None

    # 模拟数据查询
    context = {
        "name": "小龙女"
    }
    return render(request, 'book/index.html', context=context)