import os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
with open("%s\conf\%s" % (BASE_DIR, "Linux_class"), encoding="utf-8") as g1:
    data_list = [("%s" % item.split(" ")[0], int(item.split(" ")[1].strip())) for item in g1.readlines()]
with open("%s\conf\%s" % (BASE_DIR, "Python_class"), encoding="utf-8") as p1:
    pata_list = [("%s" % item.split(" ")[0], int(item.split(" ")[1].strip())) for item in p1.readlines()]
LiClass1 = ["甲","乙","丙","丁"]
LiClass2 = ["甲","乙","丙","丁"]
PyCLass1 = ["甲","乙","丙","丁"]
PyCLass2 = ["甲","乙","丙","丁"]
class Bj(object):
    def __init__(self,tuition,days):
        self.tuition=tuition
        self.days=days
    def Linux(self):
        Class=[]
        Money=[]
        print("Hello,欢迎来到linux课堂，我们的学费是%s,学习周期%s月"%(self.tuition,self.days))
        Start_linux=input("如果想成为Linux大神,请按Y，返回上一层请按N")
        if Start_linux=='Y':
            print("Hello，欢迎您成为我们的学生，来，咱们先看看咱们的班级和学费")
            for index,item in enumerate(data_list):
                print(index,item)
            Choose_Linux=input("请做出你的选择")
            if Choose_Linux.isdigit:
                Choose_Linux = int(Choose_Linux)
                if Choose_Linux < len(data_list) and Choose_Linux >= 0:
                    P_item=data_list[Choose_Linux]
                    Class.append(P_item[0])
                    print("您选择的课程%s"%P_item[0])
                    Money.append(P_item[1])
                    print("您的学费%s"%P_item[1])
                else:
                    print("请输入正确的编号")
        if Start_linux=='N':
            print("BAYBAY")
    def Python(self):
        Class=[]
        Money=[]
        print("Hello,欢迎来到python课堂，我们的学费是%s,学习周期%s月" % (self.tuition, self.days))
        Start_Python=input("如果想成为Python大神,请按Y，返回上一层请按N")
        if Start_Python=='Y':
            print("Hello，欢迎您成为我们的学生，来，咱们先看看咱们的班级和学费")
            for index,item in enumerate(pata_list):
                print(index,item)
            Choose_Python=input("请做出你的选择")
            if Choose_Python.isdigit:
                Choose_Python = int(Choose_Python)
                if Choose_Python < len(pata_list) and Choose_Python >= 0:
                    P_item=pata_list[Choose_Python]
                    Class.append(P_item[0])
                    print("您选择的课程%s"%P_item[0])
                    Money.append(P_item[1])
                    print("您的学费%s"%P_item[1])
                else:
                    print("请输入正确的编号")
        if Start_Python=='N':
            print("BAYBAY")
    def Linux_Class(self):
        Start_Class=input("Hello,欢迎您成为我们的学生，我们的班级有1班和2班，请你选择班级:")
        if Start_Class.isdigit:
            Start_Class=int(Start_Class)
            if Start_Class==1:
                if len(LiClass1) > 4:
                    print("班级人员满了，请重新选择")
                else:
                    print("Hello,欢迎成为1班学生")
                    LiClass1.append(Start_Class)
            elif Start_Class == 2:
                if len(LiClass2) > 4:
                    print("班级人员满了，请重新选择")
                else:
                    print("Hello,欢迎成为2班学生")
                    LiClass2.append(Start_Class)
    def Python_Class(self):
        Start_Class = input("Hello,欢迎您成为我们的学生，我们的班级有1班和2班，请你选择班级:")
        if Start_Class.isdigit:
            Start_Class = int(Start_Class)
            if Start_Class == 1:
                if len(PyCLass1) > 4:
                    print("班级人员满了，请重新选择")
                else:
                    print("Hello,欢迎成为1班学生")
                    PyCLass1.append(Start_Class)
            elif Start_Class == 2:
                if len(PyCLass2) > 4:
                    print("班级人员满了，请重新选择")
                else:
                    print("Hello,欢迎成为2班学生")
                    PyCLass2.append(Start_Class)
    def Linux_Teacher(self):
        Teacher_Class=input("欢迎来到Linux班级授课，我们的班级有1班和2班，请您选择:")
        if Teacher_Class.isdigit:
            Teacher_Class=int(Teacher_Class)
            if Teacher_Class==1:
                print("hello.欢迎来到1班")
                print("我们班级的学生有%s"%LiClass1)
            if Teacher_Class==2:
                print("hello.欢迎来到2班")
                print("我们班级的学生有%s"%LiClass2)
    def Python_Teacher(self):
        Teacher_Class=input("欢迎来到Python班级授课，我们有1班和2班，请您选择:")
        if Teacher_Class.isdigit:
            Teacher_Class=int(Teacher_Class)
            if Teacher_Class==1:
                print("hello.欢迎来到1班")
                print("我们班级的学生有%s"%PyCLass1)
            if Teacher_Class==2:
                print("hello.欢迎来到2班")
                print("我们班级的学生有%s"%PyCLass2)
B=Bj('8000-10000',5)
#B.Linux()
P=Bj('8000-10000',7)
#P.Python()