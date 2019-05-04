import requests, json

class main():
    def __init__(self, token):
        self.base_url = "https://osu.ppy.sh/api/"
        self.token = token
    def jsong(self, url):
        data = requests.get(url)
        return data.json()
    def user(self, name, mode, typedata=None):
        ready_url = self.base_url + "get_user?k=" + self.token + "&u=" + name + "&m=" + str(mode)
        data_get = self.jsong(ready_url)[0]
        if typedata == None:
            return data_get
        else:
            return data_get[typedata]
    def user_best(self, name, mode, typedata=None):
        ready_url = self.base_url + "get_user_best?k=" + self.token + "&u=" + name + "&m=" + str(mode) + "&limit=1"
        data_get = self.jsong(ready_url)[0]
        if typedata == None:
            return data_get
        else:
            return data_get[typedata]
    def scores(self, name, mapid, mode, typedata=None):
        ready_url = self.base_url + "get_scores?k=" + self.token + "&u=" + name + "&b=" + mapid + "&m=" + str(mode) + "&limit=1"
        data_get = self.jsong(ready_url)[0]
        if typedata == None:
            return data_get
        else:
            return data_get[typedata]
    def user_recent(self, name, mode, typedata=None):
        ready_url = self.base_url + "get_user_recent?k=" + self.token + "&u=" + name + "&m=" + str(mode) + "&limit=1"
        try:
            data_get = self.jsong(ready_url)[0]
        except:
            return "Map no found"
        if typedata == None:
            return data_get
        else:
            return data_get[typedata]
    def construct(self, root, param):
        root_url = self.base_url + root + "?k=" + self.token
        list_param = param.keys()
        ready_url = root_url
        for add_key in list_param:
            add_url = "&" + str(add_key) + "=" + param[str(add_key)]
            ready_url += add_url
        data_get = self.jsong(ready_url)
        return data_get
    def match(self, matchid):
        ready_url = self.base_url + "get_match?k=" + self.token + "&mp=" + matchid
        return data_get
    def beatmaps(self, mapid, num=None, mode=None, name=None, typedata=None):
        ready_url = self.base_url + "get_beatmaps?k=" + self.token + "&b=" + mapid
        if name != None:
            ready_url = root_url + "&u=" + name
        if mode != None:
            ready_url = root_url + "&m=" + name
        if num != None:
            ready_url = root_url + "&limit=" + num
            data_ready = data_get[num-1]
            if typedata != None:
                return data_get[typedata]
            else:
                return data_get
        else:
            ready_url = root_url + "&limit=500"
            data_get = self.jsong(ready_url)
            return data_get
        

#get_beatmaps get_replayb