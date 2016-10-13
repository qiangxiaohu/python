import os
from collections import OrderedDict
od = OrderedDict()
info={}
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
class host(object):
    def __init__(self):
        pass
    def host_one(self):
        with open("%s\conf\%s"%(BASE_DIR,"host_group"),encoding="utf-8") as h1:
            for index,line in enumerate(h1):
                H,Port,user,password=line.strip('\n').split()
                info.setdefault(index,[])
                info[index]=[H,int(Port),user,password]
        return  info
    def host_two(self):
        with open("%s\conf\%s"%(BASE_DIR,"host_grouptwo"),encoding="utf-8") as h2:
            for index,line in enumerate(h2):
                H,Port,user,password=line.strip('\n').split()
                info.setdefault(index,[])
                info[index]=[H,int(Port),user,password]
                h2_list=info[index]
        return  info
    def show_hosts(self):
        for key,value in info.items():
            od[key] = value
        for k,v in od.items():
            print("%s %s"%(k,v[0]))
    def show_info(self):
        print(info)
t = host()