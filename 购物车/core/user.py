import  os
BASEDIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
f_user = open("%s\conf\%s" % (BASEDIR, "users"), "r+", encoding="utf-8")
user_list = f_user.read().split()
class users_atm(object):
    def __init__(self):
        pass
    def login(self):
        while True:
            user_login=input("请输入你的用户名:")
            if user_login in user_list:
                user_passwd=input("请输入你的密码")
                if user_passwd == user_list[user_list.index(user_login) + 1]:
                    print("欢迎%s用户登录"%user_login)
                else:
                    print("密码错误，重新输入")
                    continue
            else:
                print("您输入的用户不存在，请重新输入")
    def add_user(self):
        while True:
            add_user_login=input("请输入你添加的用户名:")
            if add_user_login in user_list:
                print("您输入的用户%s存在"%add_user_login)
                continue
            else:
                while True:
                    add_user_passwd=input("请输入你的密码:")
                    if add_user_passwd==0:
                        print("您输入的密码为空,请重新输入")
                        continue
                    elif add_user_passwd!=0:
                        with open("%s\conf\%s" % (BASEDIR, "users_backup"), "a+", encoding="utf-8") as backup:
                            backup.write("%s %s"%(add_user_login,add_user_passwd)+'\n')
                            print("您已经添加用户%s"%add_user_login)
                            break
users_atm.login('ss')