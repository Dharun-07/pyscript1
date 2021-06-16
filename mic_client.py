#!/usr/bin/env python3

import socket
import threading
import pyaudio



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    target_ip = input('Enter IP address of server --> ')
    target_port = int(input('Enter target port of server --> '))

    s.connect((target_ip, target_port))



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
                data = s.recv(16200)
                playing_stream.write(data)
            except KeyboardInterrupt:
                s.close()
                break


    def send_data_to_server():
        while True:
            try:
                data = recording_stream.read(16200)
            except KeyboardInterrupt:
                s.close()
                break

        # start threads
    receive_thread = threading.Thread(target=receive_server_data)
    receive_thread.daemon=True
    receive_thread.start()
    send_data_to_server()
except KeyboardInterrupt:
    s.close()



