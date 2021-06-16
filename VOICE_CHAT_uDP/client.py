#!/usr/bin/env python3
import socket
import pyaudio

ip="127.0.1.1"
port=10000

sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
chunk_size = 1024 # 512
audio_format = pyaudio.paInt16
channels = 1
rate = 20000

# initialise microphone recording
p = pyaudio.PyAudio()
recording_stream =p.open(format=audio_format,channels=channels, rate=rate, input=True, frames_per_buffer=chunk_size)


while True:
            try:
                data = recording_stream.read(16200)
                sock.sendto(data,(ip,port))
            except KeyboardInterrupt:
                sock.close()
                quit()
