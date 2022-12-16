import socket, select, threading

host = socket.gethostname()
port = 5963
addr = (host, port)

inputs = []
fd_name = {}
def who_in_room(w):
    name_list = []
    for k in w:
        name_list.append(w[k])
    return name_list

def conn():
    print('wait connecting...')
    ss = socket.socket()
    ss.bind(addr)
    ss.listen(5)
    return ss

def new_coming(ss):
    client, add = ss.accept()
    print('欢迎 %s %s' % (client, add))
    wel = '''聊天室，请输入您的名称:'''
    try:
        client.send(wel.encode(encoding='utf8'))
        name = client.recv(1024).decode(encoding='utf8')
        inputs.append(client)
        fd_name[client] = name
        nameList = "当前聊天室内，有如下成员： %s" % (who_in_room(fd_name))
        client.send(nameList.encode(encoding='utf8'))
    except Exception as e:
        print(e)

def server_run():
    ss = conn()
    inputs.append(ss)
    while True:
        rList, wList, eList = select.select(inputs, [], [])
        for temp in rList:
            if temp is ss:
                new_coming(ss)
            else:
                disconnect = False
                try:
                    data = temp.recv(1024) #bytes
                    data = data.decode(encoding='utf8') #str
                    user_name = fd_name[temp] #bytes
                    data = user_name + ' say : ' + data
                    #data = data.decode('utf8')
                except socket.error:
                    data = fd_name[temp] + ' leave the room'
                    disconnect = True
                if disconnect:
                    inputs.remove(temp)
                    print(f"disconnect message:{data}")
                    for other in inputs:
                        if other != ss and other != temp:
                            try:
                                other.send(data.encode(encoding='utf8'))
                            except Exception as e:
                                print(e)
                    del fd_name[temp]
                else:
                    print(f"connect message: {data}")
                    for other in inputs:
                        if other != ss and other != temp:
                            try:
                                other.send(data.encode(encoding='utf8'))
                            except Exception as e:
                                print(e)

if __name__ == '__main__':
    server_run()