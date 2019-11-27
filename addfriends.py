# -*- coding: utf-8 -*-
from wxpy import *
import datetime

roomslist = []
bbot = Bot()

def getroom_message(n):
    #获取群的username，对群成员进行分析需要用到
    bbot.core.dump_login_status() # 显示所有的群聊信息，默认是返回保存到通讯录中的群聊
    RoomList =  bbot.core.search_chatrooms(name=n)
    if RoomList is None:
        pass
    else:
        return RoomList[0]['UserName']

def getchatrooms():
    roomslist = bbot.core.get_chatrooms()
    return roomslist


print("程序开始：",datetime.datetime.now())
for i in getchatrooms():
    roomslist.append(i['NickName'])


ChatRoom = bbot.core.update_chatroom(getroom_message('测试群'), detailedMember=True)

for i in ChatRoom['MemberList']:
    print(i)
####获取微信号
aa = ChatRoom['MemberList'][0]
bb = aa['UserName']
print(aa['NickName'])
print(bb)
##通过微信号添加好友
bbot.add_friend(user=bb)
bbot.core.send('hello',toUserName=bb)
print("程序结束：",datetime.datetime.now())