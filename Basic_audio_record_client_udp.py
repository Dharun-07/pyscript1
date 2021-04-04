#!/usr/bin/env python3
import socket
import pyaudio
import pickle
import time

s_ip=input("ENTER THE NAME OF SERvER TO GET CONNECTED")
port=10000
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)




chunk =1024
rate=44100
channels=1
format=pyaudio.paInt16
record_seconds=5

p=pyaudio.PyAudio()

stream_record=p.open(format=format,rate=rate,channels=channels,input=True,frames_per_buffer=chunk)
stream=p.open(format=format,rate=rate,channels=channels,output=True)
print("recording")

frame=[]
list=[1,2,3,4,5,6,7,8,9]

for i in range(0,int(rate/chunk*record_seconds)):
    data=stream_record.read(chunk)
    frame.append(data)
for data in frame:
    sock.sendall(data,("127.0.1.1",port))
    '''frame=pickle.dumps(frame)
conn.send(frame)'''
sock.sendto(b"completed",(s_ip,port))

sock.close()

stream.stop_stream()
stream.close()
p.terminate
sock.close()
print("connection closed")