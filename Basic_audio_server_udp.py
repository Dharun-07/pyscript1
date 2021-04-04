#!/usr/bin/env python3

import socket
import wave
import pickle
import pyaudio
import time

h_name=socket.gethostname()
h_ip=socket.gethostbyname((h_name))
port=10000
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind((h_ip,port))
print("connected")

'''format=pyaudio.paInt16
channels=1
rate=44100
wav_output_filename="output.wav"
p=pyaudio.PyAudio
frames=[]
chunk=1024*4
#stream = p.open(format=format,channels=channels,rate=rate,output=True,frames_per_buffer=chunk)
try:
    while(True):
        data=conn.recv(2048)
        #stream.write(data)
        frames.append(data)

    print(frames)
    with wave.open("wav_output_filename",'wb') as wf:
        wf.setchannels(channel)
        wf.setampwidth(p.get_sample_size(format))
        wf.setframerate(rate)
        wf.writeframes(b''.join(frames))
    stream.stop_stream()
    stream.close()
    p.terminate()

except KeyboardInterrupt:
    conn.close()
    stream'''

sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

frame=[]
while(sock.recv(1024)):
    data=sock.recvfrom(1024)
    if(data==b"completed"):
        sock.close()
        break
    frame.append(data)

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



for data in frame:
    stream.write(data)

sock.close()


stream.stop_stream()
stream.close()
p.terminate
sock.close()
print("connection closed")
