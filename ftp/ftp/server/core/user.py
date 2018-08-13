import os
import sys
import hashlib
from ftp.client.conf.conf import configuration
class UserInfo:
    __instance=None

    server_path_lst=sys.path[0].split(os.sep)[:-1]
    server_path_lst.extend(["db","user_info"])
    server_path=(os.sep).join(server_path_lst)
    ftp_root=configuration["auth_key"]
    coding=configuration["coding"]

    def __new__(cls, *args, **kwargs):
        if UserInfo.__instance is None:
            UserInfo.__instance =object.__new__(cls,*args,**kwargs)
            cls.load_user_info()
        return UserInfo.__instance


    @classmethod
    def get_pwd(cls,pwd):
        hash=hashlib.md5(pwd.encode(encoding=cls.coding))
        hash.update(cls.auth_key.encode(encoding=cls.coding))
        return hash.hexdigest()





