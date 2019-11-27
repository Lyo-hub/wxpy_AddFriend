# -*- coding: utf-8 -*-
import itchat
import time
from wxpy import *

import datetime
from itchat.content import TEXT
roomslist = []
# itchat.auto_login(hotReload=True)
bbot = Bot()

def getroom_message(n):
    #获取群的username，对群成员进行分析需要用到
    bbot.core.dump_login_status() # 显示所有的群聊信息，默认是返回保存到通讯录中的群聊
    RoomList =  bbot.core.search_chatrooms(name=n)
    if RoomList is None:
        pass
        #print("{0} group is not found!".format(name))
    else:
       # print('取得：',RoomList[0]['UserName'])
        return RoomList[0]['UserName']

def getchatrooms():
    #获取群聊列表
    roomslist = bbot.core.get_chatrooms()
    #print('列表',roomslist)
    return roomslist


print("程序开始：",datetime.datetime.now())
for i in getchatrooms():
    roomslist.append(i['NickName'])

# bbot.groups(update=True)

ChatRoom = bbot.core.update_chatroom(getroom_message('测试群'), detailedMember=True)
#print("ChatRoom",ChatRoom)

for i in ChatRoom['MemberList']:
    print(i)
aa = ChatRoom['MemberList'][0]
print("====================================")
bb = aa['UserName']
print(aa['NickName'])
print(bb)
#
# bbot = Bot()
print("=====================================")
bbot.add_friend(user=bb)
bbot.core.send('hello',toUserName=bb)
print("程序结束：",datetime.datetime.now())