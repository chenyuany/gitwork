#! /usr/bin/env python
#coding=utf-8

import json

u'''解码json文件'''
class jsonTranscoding():
    
    u'''读取文件'''
    def loadFont(self):
        f = open("\\testIsomp\\common\\config.json","r")
        setting = json.load(f)
        return setting
    
    u'''获取ip'''
    def get_app_ip(self):
        t = self.loadFont()
        app_dict = t["APP"]
        app_ip = app_dict['appip']
        return app_ip
    
    u'''获取远程服务器url和浏览器类型'''
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

    u'''获取ip'''
    def get_app_ip_test(self):
        t = self.loadFont()
        ip_num = len(t["APP"])
        appip_list = []
        for ip_index in range(ip_num):
            appip = t["APP"][ip_index]["appip"]
            appip_list.append(appip)  
        return appip_list
    
    u'''获取详细的浏览器类型'''
    def get_brower_type(self):
        t = self.loadFont()
        brower_num = len(t["BROWER"])
        brower_type_list = []
        for brower_index in range(brower_num):
            brower_detail_type = t["BROWER"][brower_index]["detailType"]
            brower_type_list.append(brower_detail_type)  
        return brower_type_list
        


#print jsonTranscoding().get_app_ip_test()
#print jsonTranscoding().set_brower()
#print jsonTranscoding().get_brower_type()