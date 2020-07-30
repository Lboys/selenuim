import requests, json
from unittest import mock


def http_request_baidu():
    '''
    使用requests接口请求第三方库
    :return:
    '''
    res = requests.get("http://www.baidu.com")
    return res.status_code


if __name__ == '__main__':
    print("打印原http请求响应码:", http_request_baidu())
    # mock需要先声明一个实例，场景：如果就是http_request_baidu函数没有开发完成，这时又要调用它
    # 那么申请的mock实例就要与之同名，也就是覆盖它原来的功能
    # test如果不同名，也就是无法覆盖，它什么都不是
    http_request_bai = mock.Mock(return_value="201")
    print("第一个是mock的状态码{},第二个跟mock的不一样：{},也就不是覆盖,而是原请求的状态码".format(http_request_bai(), http_request_baidu()))


http_request_baidu = mock.Mock(return_value="404")  # 返回的是一个字符串，如果是想要json格式的呢，要怎么做？
print("被覆盖后的请求响应状态码：", http_request_baidu())
http_request_baidu = mock.Mock(return_value='{"status":1,"msg":"成功"}')
print("打印响应的json格式输出", http_request_baidu())  # 实际输出的还是字符串，所以需要转dict
http_request_baidu = mock.Mock(return_value=json.loads('{"status":1,"msg":"成功"}'))
print("查看被mock的数据格式时候转成python对象：", type(http_request_baidu()))
