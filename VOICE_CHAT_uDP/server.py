#!/usr/bin/env python3
import socket
import pyaudio


sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind(("127.0.1.1",10000))

chunk_size = 1024 # 512
audio_format = pyaudio.paInt16
channels = 1
rate = 20000

        # initialise microphone recording
p = pyaudio.PyAudio()
playing_stream = p.open(format=audio_format,channels=channels, rate=rate, output=True, frames_per_buffer=chunk_size)

while True:
    try:
        data,addr=sock.recvfrom(16200)
        playing_stream.write(data)
    except KeyboardInterrupt:
        sock.close()
        quit()


