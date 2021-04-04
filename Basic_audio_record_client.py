#!/usr/bin/env python3
import socket
import pyaudio
import pickle
import time

s_ip=input("ENTER THE NAME OF SERvER TO GET CONNECTED")
port=10000
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect((s_ip,port))

chunk =1024
rate=44100
channels=1
format=pyaudio.paInt16
record_seconds=5
p=pyaudio.PyAudio()
stream=p.open(format=format,rate=rate,channels=channels,output=True)

'''chunk=1024*4
format=pyaudio.paInt16
channels=1
rate=44100
record_seconds=3
p=pyaudio.PyAudio()
stream = p.open(format=format,channels=channels,rate=rate,input=True,frames_per_buffer=chunk)
print("Recording")
try:
    while(True):
        data=stream.read(chunk)
        sock.send(data)
except KeyboardInterrupt:
    sock.close()
    print("CONNECTION TERMINATED")'''

frame=[]
try:
    while(sock.recv(1024)):
        data=sock.recv(1024)
        if(data==b"completed"):
            sock.close()
            break
        frame.append(data)

    for data in frame:
        stream.write(data)
except KeyboardInterrupt:
    sock.close()


stream.stop_stream()
stream.close()
p.terminate
sock.close()
print("connection closed")

