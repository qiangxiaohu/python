import os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
atm_user = open("%s\conf\%s" % (BASE_DIR, "ATM"), "r+", encoding="utf-8")
user_list = atm_user.read().split()
class atm_tired(object):
    def __init__(self):
        pass
    def show_atm(self):
        money=0
        while True:
            atm_login=input("请输入你要查询的卡号:exit退出")
            if atm_login in user_list:
                atm_passwd=input("请输入你的密码:")
                if atm_passwd == user_list[user_list.index(atm_login) + 1 ]:
                    money=user_list[user_list.index(atm_login) + 2]
                    print(money)
                    print("您的账户余额%s"%(money))
                    return money
                else:
                    print("密码错误")
            if atm_login=='exit':
                return money
            else:
                print("卡号不存在")
    def deposit(self):
        while True:
            atm_login=input("请输入你的卡号:,exit退出")
            if atm_login=='exit':
                break
            if atm_login in user_list:
                atm_passwd=input("请输入你的密码:")
                if atm_passwd == user_list[user_list.index(atm_login) + 1]:
                    money=user_list[user_list.index(atm_login) + 2]
                    money=int(money)
                    print("您的账户余额%s"%(money))
                    atm_deposit = input("请输存入你要存款的金额")
                    if atm_deposit == 0:
                        print("您输入为空，请重新输入")
                    elif atm_deposit != 0:
                        atm_deposit=int(atm_deposit)
                        sally = (money + atm_deposit)
                        print(sally)
                        with open("%s\conf\%s" % (BASE_DIR, "deposit_backup"), "a+", encoding="utf-8") as backup:
                            backup.write("%s %s %s" % (atm_login, atm_passwd, sally))
                        print("您存入了%s,余额%s" % (atm_deposit, sally))
                else:
                    print("密码错误")
                    continue
            else:
                print("卡号不存在")
                continue
    def draw(self):
        while True:
            atm_login=input("请输入你的卡号:,exit退出")
            if atm_login=='exit':
                break
            if atm_login in user_list:
                atm_passwd=input("请输入你的密码:")
                if atm_passwd == user_list[user_list.index(atm_login) + 1 ]:
                    money=user_list[user_list.index(atm_login) + 2]
                    print(money)
                    print("您的账户余额%s"%(money))
                    atm_draw=input("请输入你要取款的金额")
                    atm_draw=int(atm_draw)
                    atm_drawuser = user_list[user_list.index(atm_login) + 2]
                    atm_drawuser=int(atm_drawuser)
                    if atm_drawuser >= atm_draw:
                        print("您取款的金额%s"%atm_draw)
                        sally=atm_drawuser-atm_draw
                        print("您当前的余额%s"%sally)
                        with open("%s\conf\%s" % (BASE_DIR, "draw_backup"), "a+", encoding="utf-8") as backup:
                            backup.write("%s %s %s"%(atm_login,atm_passwd,sally))
                    else:
                        print("余额不足")
                        continue
                else:
                    print("密码错误")
                    continue