def main():
    while True:
        Start_main=input("欢迎来到Abeo Hu总教育，如果您是应聘老师，选择1，学生请选择2,exit退出:")
        if Start_main=='exit':
            break
        if Start_main.isdigit():
            Start_main=int(Start_main)
            if Start_main==1:
                Start_main_Teacher=input("欢迎来到老师应聘平台,北京地区选择1，上海地区选择2,返回请按Y:")
                if Start_main_Teacher=='Y':
                    break
                if Start_main_Teacher.isdigit:
                    Start_main_Teacher=int(Start_main_Teacher)
                    if Start_main_Teacher==1:
                        import  T_eacher
                        T_eacher.B.BJHello()
                        break
                    elif Start_main_Teacher==2:
                        import T_eacher
                        T_eacher.B.ShHello()
                        break
                    else:
                        print("请输入正确的参数")
                        continue
            if Start_main==2:
                Start_main_Student=input("欢迎来到学生报名平台，北京地区选择1，上海地区选择2,返回请按Y:")
                if Start_main_Student=='Y':
                    break
                if Start_main_Student.isdigit:
                    Start_main_Student=int(Start_main_Student)
                    if Start_main_Student==1:
                        import student
                        student.B.BJ_Student()
                    elif Start_main_Student==2:
                        import student
                        student.B.SH_Student()
                    else:
                        print("请输入正确的参数")
                        continue
main()