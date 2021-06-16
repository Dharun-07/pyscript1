#!/usr/bin/env python3
import socket
import threading
import pyaudio

ip = socket.gethostbyname(socket.gethostname())
print(ip)
try:
    port = int(input('Enter port number to run on --> '))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((ip, port))

    connections = []
    sock.listen(1)
    s,addr=sock.accept()

    chunk_size = 1024  # 512
    audio_format = pyaudio.paInt16
    channels = 1
    rate = 20000

        # initialise microphone recording
    p = pyaudio.PyAudio()
    playing_stream = p.open(format=audio_format, channels=channels, rate=rate, output=True,
                                      frames_per_buffer=chunk_size)
    recording_stream = p.open(format=audio_format, channels=channels, rate=rate, input=True,
                                        frames_per_buffer=chunk_size)

    print("Connected to Server")
    def receive_server_data():
        while True:
            try:
                data = s.recv(1024)
            except KeyboardInterrupt:
                sock.close()
                break


    def send_data_to_server():
        while True:
            try:
                data = recording_stream.read(16200)
                sock.sendall(data)
            except KeyboardInterrupt:
                sock.close()
                break

            # start threads
    receive_thread = threading.Thread(target=receive_server_data)
    receive_thread.daemon=True
    receive_thread.start()
    send_data_to_server()
except KeyboardInterrupt:
    sock.close()




