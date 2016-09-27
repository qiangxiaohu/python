import os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
with open("%s\conf\%s" % (BASE_DIR, "goods"), encoding="utf-8") as g1:
    data_list = [("%s" % item.split(" ")[0], int(item.split(" ")[1].strip())) for item in g1.readlines()]
class Mythred(object):
    def __init__(self,name):
        self.name=name
    def show(self):
        for index, item in enumerate(data_list):
            print(index, item)
    def add_shop(self):
        while True:
            admin_shop=input("请输入你要添加的商品和价格,exit退出")
            if admin_shop=='exit':
                break
            NUM=len(admin_shop)-len(admin_shop.replace(' ',''))
            NUM1=len(admin_shop.replace(' ',''))
            if admin_shop==0:
                print("您输入为空，请重新输入")
                continue
            elif NUM==1 and admin_shop.split()[1]:
                with open("%s\conf\%s" % (BASE_DIR, "goods_backup"),"a+",encoding="utf-8") as backup:
                    backup.write("%s %s"%(admin_shop.split()[0],admin_shop.split()[1])+'\n')
                    print(admin_shop[0])
                    print("您已经添加商品%s到系统"%(admin_shop[0]))
            else:
                print("您输入错误，格式为商品价格")
                continue
    def user_shop(self):
        shoping=[]
        money=[]
        exit = False
        while True:
            user_shoping=input("请输入你要购买商品的编号,exit结算:")
            if user_shoping == "exit":
                return  sum([ int(m) for m in money])
            if user_shoping.isdigit:
                user_shoping=int(user_shoping)
                if user_shoping < len(data_list) and user_shoping>=0:
                    p_item=data_list[user_shoping]
                    shoping.append(p_item[0])
                    print("加入%s到购物车"%p_item[0])
                    money.append(p_item[1])
                    print("价格为%s"%p_item[1])
                else:
                    print("请输入正确的编号")
            elif user_shoping=='exit':
                break
            else:
                print("请输入数字")