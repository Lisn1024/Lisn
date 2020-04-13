import requests
import json

class ConfigHttp(object):

    def get(self,url,param):
        res = requests.get(url=url,params=eval(param))
        print(res.text)
        dict = json.loads(res.text)
        errorcode = dict["errorCode"]
        return errorcode
    def post(self,url,param):
        res = requests.post(url=url,data=eval(param))
        print(res.text)
        dict = json.loads(res.text)
        errorcode = dict["errorCode"]
        return errorcode

    def getRequest(self,method,url,param):
        if str(method) == "get":
            return self.get(url,param)
        elif str(method) == "post":
            return self.post(url,param)
        
        
if __name__ == '__main__':
    send = ConfigHttp()
    param = {'username': 'liangchao03', 'password': '123456', 'repassword': '123456'}
    print(send.post('https://www.wanandroid.com/user/register', param))