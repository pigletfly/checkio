# encoding: utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
import requests
import json

appid = "wxfe94f93c3aa355bf"
secret = "dbed9355eaf42abfc51590538937642f"
access_url = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={appid}&secret={secret}"
create_menu_url = "https://api.weixin.qq.com/cgi-bin/menu/create?access_token={token}"
get_menu_url = "https://api.weixin.qq.com/cgi-bin/menu/get?access_token={token}"
del_menu_url = "https://api.weixin.qq.com/cgi-bin/menu/delete?access_token={token}"


def get_access_token():
    url = access_url.format(appid=appid, secret=secret)
    r = requests.get(url)
    return r.json().get('access_token')


def generate_menu(token):
    menus = {"button": [{
        "name": "查询食物",
        "type": "click",
        "key": "0"
    }, {
        "name": "我的记录",
        "sub_button": [
            {
                "type": "click",
                "name": "剩余轻币",
                "key": "1"
            },
            {
                "type": "click",
                "name": "历史饮食",
                "key": "2"
            },{
                 "type": "click",
                "name": "历史体重",
                "key": "3"
            },{
                 "type": "click",
                "name": "个人资料",
                "key": "4"
            },{
                 "type": "click",
                "name": "绑定或注册用户",
                "key": "5"
            }]
    }, {
        "name": "更多服务",
         "sub_button": [
            {
                "type": "click",
                "name": "轻币工具",
                "key": "6"
            },
            {
                "type": "click",
                "name": "意见反馈",
                "key": "7"
            },{
                 "type": "click",
                "name": "如何记录",
                "key": "8"
            }]
    }]}
    headers = {'content-type': 'application/json; charset=utf8'}
    url = create_menu_url.format(token=token)
    print json.dumps(menus)
    r = requests.post(url, data=json.dumps(
        menus, ensure_ascii=False), headers=headers)
    print r.text


def get_menu(token):
    url = get_menu_url.format(token=token)
    r = requests.get(url)
    print r.json()


def delete_menus(token):
    url = del_menu_url.format(token=token)
    r = requests.get(url)
    print r.json()


def main():
    token = get_access_token()
    generate_menu(token)
    get_menu(token)
    # delete_menus(token)

if __name__ == '__main__':
    main()
