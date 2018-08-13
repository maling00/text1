import socketserver
import json
from ftp.server.core.server import Views


class MySever(socketserver.BaseRequestHandler):
    def my_send(self, content):
        content = json.dumps(content)
        send_content = content.encode("utf-8")
        try:
            self.conn.send(send_content)
        except:
            print("客户端由于网络原因断开连接")
            return False
    def my_recv(self):
        try:
            json_msg = self.conn.recv(1024).decode("utf-8")
            msg = json.loads(json_msg)
            return msg
        except Exception as e:
            print(e)
            return False
    def handle(self):
        self.conn = self.request
        flag = True
        while flag:
            ret = self.my_recv()
            if type(ret) is dict and ret["operation"] == "myquit":
                flag = False
                pass