from collections import OrderedDict
import paramiko,threading,time
import hosts
portss=22
print(type(portss))
def run(hostnames,ports,name,passwd):
    tem=input("请输入你要执行的命令")
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=hostnames, port=ports, username=name, password=passwd)
    stdin, stdout, stderr = ssh.exec_command(tem)
    result = stdout.read()
    print(result.decode())
    ssh.close()
def run_ftp(hostnames,ports,name,passwd):
    import paramiko
    transport = paramiko.Transport((hostnames,ports))
    transport.connect(username=name, password=passwd)
    SFTP = paramiko.SFTPClient.from_transport(transport)
    SFTP_cholice=input("请您选择您的功能,1是上传，2是下载")
    if SFTP_cholice.isdigit:
        SFTP_cholice=int(SFTP_cholice)
        if SFTP_cholice=='1':
            SFTP_put_source=input("请输入你要上传的源目录")
            SFTP_put_intent=input("请输入你要上传的目的地址")
            SFTP.put(SFTP_put_source,SFTP_put_intent)
        if SFTP_cholice=='2':
            SFTP_get_source=input("请输入你要下载的源目录")
            SFTP_get_intent=input("请输入你要下载的目的地址")
            SFTP.put(SFTP_get_source,SFTP_get_intent)
    else:
        print("请输入数字")
    SFTP.put('/tmp/tt.py', '/tmp/test.py')
    SFTP.get('remove_path', 'localhost')
    transport.close()
def decideone(info):#主机密码模块
    while True:
        batch=print("由于是批量执行主机组，请您通过主机编号输入主机名和密码:")
        ip_number =  int(input("ip_number:"))
        host_msg = info.get(ip_number)
        host_port = int(input("port:"))
        if host_port==host_msg[1]:
            host_name=input("name:")
            if host_name==host_msg[2]:
                host_passwd=input("passwd:")
                if host_passwd==host_msg[3]:
                    print("登陆成功,请您继续输入批量执行的机器")
                    break
                else:
                    print("输入错误")
                    continue
            else:
                print("输入错误")
                continue
        else:
            print("输入错误")
            continue
def decideone_boss(info):#批量模块
    decideone(info)
    print("正在批量执行命令")
    for key,value in info.items():
        print('''---主机%s信息'''%key)
        t1 = threading.Thread(target=run, args=tuple(info[key]))
        t1.start()
        t1.join()
def decideone_SFTP(info):#批量模块
    decideone(info)
    for key,value in info.items():
        t1 = threading.Thread(target=run_ftp, args=tuple(info[key]))
        t1.start()
        t1.join()
