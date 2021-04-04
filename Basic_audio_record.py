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
sock.listen(1)
conn,addr=sock.accept()
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
try:
    for data in frame:
        conn.sendall(data)
    '''frame=pickle.dumps(frame)
conn.send(frame)'''
    conn.send(b"completed")
except KeyboardInterrupt:
    conn.close()
    sock.close()
    quit()

stream.stop_stream()
stream.close()
p.terminate
conn.close()
sock.close()
print("connection closed")