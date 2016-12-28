# coding:utf-8
import socket
HOST = 'localhost'
PORT = 843
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #用什么方式通信，使用的套接字类型
s.connect((HOST,PORT)) #连接host和post

# 组装信息
message = '{"wid":22499,"content":"你太逗比了！！！","id":45,"param":"0,1482302752,28,3407667,1,4,45,%E5%B1%8C%E4%B8%9D"}'
s.sendall(bytes(message,encoding='utf8'))
data = s.recv(1024)
s.close()
