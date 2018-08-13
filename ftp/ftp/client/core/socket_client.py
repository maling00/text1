import json
import socket

from ftp.client.conf.conf import configuration


class MySocketClient:
    __instance=None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance =object.__new__(cls,*args,**kwargs)
            ip_port =(configuration.get("serve_ip"),configuration.get("serve_port"))
            cls.sk=socket.socket()
            cls.conn=cls.sk.connect(ip_port)
        return cls.__instance

    @classmethod
    def sk_send(cls,content):
        str_content=json.dumps(content)
        send_content=bytes(str_content,encoding="utf-8")
        cls.sk.sendall(send_content)

    @classmethod
    def sk_recv(cls):
        data =cls.sk.recv(1024).decode("utf-8")
        return json.loads(data)




