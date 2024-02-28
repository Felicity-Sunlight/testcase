import requests


def test_weekly():

    # 发送get请求
    url = "https://tenapi.cn/v2/weekly"
    data = {"num": 200}
    rep = requests.request("post", url=url, params=data)
    print(rep.json())
