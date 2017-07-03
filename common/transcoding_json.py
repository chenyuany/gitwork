#! /usr/bin/env python
#coding=utf-8

import json

class jsonTranscoding():
    
    def loadFont(self):
        f = open("\\testIsomp\\common\\data.json","r")
        setting = json.load(f)
        return setting
 
    def get_app_ip(self):
        t = self.loadFont()
        app_dict = t["APP"]
        app_ip = app_dict['appip']
        return app_ip

    def set_brower(self):
        t = self.loadFont()
        key_num = len(t["BROWER"])
        remote_dict = {}
        for key_index in range(key_num):
            brower_key = t["BROWER"][key_index]
            ip = brower_key["ip"]
            port = brower_key["port"]
            type = brower_key["type"]

            dict_value = "http://" + str(ip) +":" + str(port) + "/wd/hub"
        
            remote_dict[dict_value] = type

        return remote_dict

#print jsonTranscoding().get_app_ip()
#print jsonTranscoding().set_brower()
