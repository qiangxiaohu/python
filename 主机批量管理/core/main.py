import operation
def run():
    while True:
        login=input("Hello,欢迎来到堡垒机项目,选择主机组请按1，退出请exit")
        if login.isdigit:
            login=int(login)
            if login==1:
                login_host=input('''
                --------当前主机组--------
                1 MYSQL
                2 Nginx
                ----------请选择----------
                ''')
                if login_host.isdigit:
                    login_host=int(login_host)
                    if login_host==1:
                        import hosts
                        info=hosts.host.host_one(1)
                        print('''-------当前主机有-------
                        ''')
                        hosts.host.show_hosts(1)
                        operation.decideone(info)
                        host_1cholice=input("请选择您的功能，ssh选择1，ftp选择2")
                        if host_1cholice.isdigit:
                            host_1cholice=int(host_1cholice)
                            if host_1cholice=='1':
                             operation.decideone_boss(info)
                            elif host_1cholice=='2':
                             operation.decideone_SFTP(info)
                            else:
                                print("请输入正确选择")
                                continue
                        else:
                            print("请输入正确选择")
                            continue
                    elif login_host==2:
                        import hosts
                        info = hosts.host.host_one(1)
                        print('''-------当前主机有-------
                                          ''')
                        hosts.host.show_hosts(1)
                        operation.decideone(info)
                        host_2cholice = input("请选择您的功能，ssh选择1，ftp选择2")
                        if host_2cholice.isdigit:
                            host_1cholice = int(host_2cholice)
                            if host_1cholice == '1':
                                operation.decideone_boss(info)
                            elif host_1cholice == '2':
                                operation.decideone_SFTP(info)
                            else:
                                print("请输入正确选择")
                        else:
                            print("请输入正确选择")
                        hosts.host.show_hosts(1)
                elif login_host=='exit':
                    print("退出")
        elif login=='exit':
            print("正在退出")
            break
        else:
            print("输入不正确")
            continue
run()

