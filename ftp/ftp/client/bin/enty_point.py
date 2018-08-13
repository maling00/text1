from ftp.client.core.auth_client import MyClient
entry_operate =["登录","注册","退出"]
while True:

    client=MyClient()
    entry_operate_dic={"登录":client.login,"注册":client.register,"退出":client.myquit}
    for num,operate in enumerate(entry_operate,1):
        print(num,operate)
    oper=input("请输入你要操作的序号：")


    try:
        func = entry_operate_dic[entry_operate[int(oper) - 1]]
    except:
        print("您输入的序号有误")
        continue
    ret=func()
