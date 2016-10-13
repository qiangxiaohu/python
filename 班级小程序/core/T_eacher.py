class Teacher(object):
    def __init__(self,teacher):
        self.teacher=teacher
    def BJHello(self):
        print("Hello,我是你们的老师Mr%s"%self.teacher)
        import Sc_BJ
        Choose_Class=input("我们有Linux和Python班，Linux选择1，Python选择2")
        if Choose_Class.isdigit:
            Choose_Class=int(Choose_Class)
            if Choose_Class==1:
                Sc_BJ.B.Linux_Teacher()
            elif Choose_Class==2:
                Sc_BJ.B.Python_Teacher()
            else:
                print("输入错误，请重新输入")
    def ShHello(self):
        print("Hello,我是你们的老师Mr%s" % self.teacher)
        import Sc_SH
        Sc_SH.B.Go_Teacher()
B=Teacher('xiaohu')
#B.ShHello()
#B.BJHello()