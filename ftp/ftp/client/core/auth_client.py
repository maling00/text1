from ftp.client.core.socket_client import MySocketClient


class MyClient():
    def __init__(self):
        self.sk = MySocketClient()
        self.name = None

    # 登录
    def login(self):

        flag = True
        while flag:
            usrname = input("请输入用户名，按q退出登录：")
            if usrname == "q":
                return {"operation": "login", "result": False}
            passwd = input("请输入密码：")
            if usrname and passwd:
                info = {"operation": "login", "username": usrname, "password": passwd}
                self.sk.sk_send(info)
                ret = self.sk.revc()
                print("\033[1;32;34m %s \033[0m" % ret[1])
                if ret[0]:
                    self.name = usrname
                    return {"operation": "login",
                            "result": True,
                            "root_path": ret[2]}

    # 注册
    def register(self):

        while True:
            usrname = input("请输入您要注册的用户名，按q退出注册：").strip()
            if usrname == "q":
                return {"operation": "register", "result": False}
            elif usrname:
                while True:
                    passwd = input("请设置登录密码：")
                    passwd1 = input("请再次输入密码确定：")
                    if passwd == passwd1:

                        info = {"operation": "register", "username": usrname, "password": passwd}
                        self.sk.sk_send(info)
                        ret = self.sk.sk_recv()
                        print("\033[1;32;42m %s \033[0m" % ret[1])
                        if ret[0]:
                            self.name = usrname
                            return {"operation": "register",
                                    "result": True,
                                    "root_path": ret[2]}
                        break
                    else:
                        print("两次输入的密码不一致，请重新输入")

def myquit(self):
    self.sk.sk_send({"operation":"myquit"})
    self.sk.close()
    exit()
