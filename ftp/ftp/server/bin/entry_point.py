import socketserver

from ftp.server.conf.conf import *
from ftp.server.core import socket_server

def main():
    sever=socketserver.ThreadingTCPServer(
        (configuration.get("server_ip"),
         configuration.get("server_port")),
        socket_server.MyServer)

    sever.serve_forever()
if __name__ =="__main__":
    main()



