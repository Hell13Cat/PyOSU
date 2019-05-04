import requests, json

class Errorgen(Exception):
    def __init__(self, text):
        self.txt = text


class main():
    def __init__(self, token):
        self.base_url = "https://osu.ppy.sh/api/"
        self.token = token
    def jsong(self, url):
        try:
            data=requests.get(url)
        except:
            raise Errorgen("No Connect to server")
        return data.json()
    def get_user(self, name, mode, typedata=None):
        ready_url = self.base_url + "get_user?k=" + self.token + "&u=" + name + "&m=" + str(mode)
        data_get = self.jsong(ready_url)[0]
        if typedata==None:
            return data_get
        else:
            try:
                return data_get[typedata]
            except:
                raise Errorgen("Type data error: " + typedata)
    def get_user_best(self, name, mode, typedata=None):
        ready_url = self.base_url + "get_user_best?k=" + self.token + "&u=" + name + "&m=" + str(mode) + "&limit=1"
        data_get = self.jsong(ready_url)[0]
        if typedata==None:
            return data_get
        else:
            try:
                return data_get[typedata]
            except:
                raise Errorgen("Type data error: " + typedata)
    def get_user_recent(self, name, mode, typedata=None):
        ready_url = self.base_url + "get_user_recent?k=" + self.token + "&u=" + name + "&m=" + str(mode) + "&limit=1"
        try:
            data_get = self.jsong(ready_url)[0]
        except:
            return "Map no found"
        if typedata==None:
            return data_get
        else:
            try:
                return data_get[typedata]
            except:
                raise Errorgen("Type data error: " + typedata)