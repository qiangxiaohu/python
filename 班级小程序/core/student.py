class Student(object):
    def __init__(self,name):
        self.name=name
    def BJ_Student(self):
        print("欢迎学生%s"%self.name)
        import Sc_BJ
        Choose=input("请您选择课程，Linux选择1，Python选择2")
        if Choose.isdigit:
            Choose=int(Choose)
            if Choose==1:
                Sc_BJ.B.Linux()
                Sc_BJ.B.Linux_Class()
            elif Choose==2:
                Sc_BJ.B.Python()
                Sc_BJ.B.Python_Class()
    def SH_Student(self):
        print("欢迎学生%s" % self.name)
        import Sc_SH
        Sc_SH.B.GO()
        Sc_SH.B.Go_Class()
B=Student('xiaohu')
B.SH_Student()