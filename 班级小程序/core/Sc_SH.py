import os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
with open("%s\conf\%s" % (BASE_DIR, "Go_class"), encoding="utf-8") as g1:
    data_list = [("%s" % item.split(" ")[0], int(item.split(" ")[1].strip())) for item in g1.readlines()]
Go_Class1=["甲","乙","丙","丁"]
Go_Class2=["甲","乙","丙","丁"]
class Sh(object):
    def __init__(self,tuition,days):
        self.tuition=tuition
        self.days=days
    def GO(self):
        Class = []
        Money = []
        print("Hello,欢迎来到GO课堂，我们的学费是%s,学习周期%s月"%(self.tuition,self.days))
        Start_linux = input("如果想成为Go大神,请按Y，返回上一层请按N")
        if Start_linux == 'Y':
            print("Hello，欢迎您成为我们的学生，来，咱们先看看咱们的班级和学费")
            for index, item in enumerate(data_list):
                print(index, item)
            Choose_Linux = input("请做出你的选择")
            if Choose_Linux.isdigit:
                Choose_Linux = int(Choose_Linux)
                if Choose_Linux < len(data_list) and Choose_Linux >= 0:
                    P_item = data_list[Choose_Linux]
                    Class.append(P_item[0])
                    print("您选择的课程%s" % P_item[0])
                    Money.append(P_item[1])
                    print("您的学费%s" % P_item[1])
                else:
                    print("请输入正确的编号")
        if Start_linux == 'N':
            print("BAYBAY")
    def Go_Class(self):
        Start_Class=input("Hello,欢迎您成为我们的学生，我们的班级有1班和2班，请你选择班级:")
        if Start_Class.isdigit:
            Start_Class=int(Start_Class)
            if Start_Class==1:
                if len(Go_Class1) > 4:
                    print("班级人员满了，请重新选择")
                else:
                    print("Hello,欢迎成为1班学生")
                    Go_Class1.append(Start_Class)
            elif Start_Class == 2:
                if len(Go_Class2) > 4:
                    print("班级人员满了，请重新选择")
                else:
                    print("Hello,欢迎成为2班学生")
                    Go_Class2.append(Start_Class)
    def Go_Teacher(self):
        Teacher_Class=input("欢迎来到GO班级授课，我们的班级有1班和2班，请您选择:")
        if Teacher_Class.isdigit:
            Teacher_Class=int(Teacher_Class)
            if Teacher_Class==1:
                print("hello.欢迎来到1班")
                print("我们班级的学生有%s"%Go_Class1)
            if Teacher_Class==2:
                print("hello.欢迎来到2班")
                print("我们班级的学生有%s"%Go_Class2)
B=Sh('8000-10000',5)