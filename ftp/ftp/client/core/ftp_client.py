from ftp.client.core.socket_client import MySocketClient
from ftp.client.conf .conf import  configuration
class FTP_client:
    def __init__(self,usr,path):
        self.usr=usr
        self.root_path=path
        self.current_path=path
        self.sk=MySocketClient()
        self.coding=configuration["coding"]

    def get_dir(self):
        self.sk.sk_send({"operation":"ls",
                         "current_path":self.current_path,
                         "username":self.usr
                         })
        data=self.sk.sk_recv()
        return data

    def show_ls(self,data):
        if data[0] and type(data[1]) is dict and data[1]["file"] or data[1]["dir"]:
            if data[1]["dir"]:
                print("文件夹")
                for i in data[1]["dir"]:
                    print("\t,i")
            if data[1]["file"]:
                print("文件")
                for i in data[1]["file"]:
                    print("\t",i)
            elif data[0]:
                print("当前目录为空")
            else:
                print(data[1])
    def fule_send(self):  pass



    def upload(self):pass

    def download(self):pass


    def ls(self):
        data=self.get_dir()
        self.show_ls(data)

    def cd_back(self):pass

    def cd(self):
        data=self.get_dir()
        while True:
            self.show_ls(data)
            dir_name=input("请输入要进入的文件夹名，按q退出本次操作：")
            if dir_name=="q":
                return
            elif dir_name.strip() in data[1]["dir"]:
                self.current_path=os.path.join(self.current_path,dir_name)
                data =self.get_dir()
                print("已经进入新目录：%s"%dir_name)
                self.show_ls(data)
                return
            else:
                print("对不起，您输入的文件夹不存在，请改正")










