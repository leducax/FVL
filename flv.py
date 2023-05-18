import os
import time
import webbrowser

def set_console_title(title):
    if os.name == "posix":
        # Terminal ANSI escape sequence
        print(f"\033]0;{title}\007", end="")
    elif os.name == "nt":
        # Windows command prompt title change
        os.system(f"title {title}")

def slow_type(message, delay):
    for char in message:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

print(""" \033[92m
 _______ _    _    _ 
(_______) |  | |  | |
 _____  | |  | |  | |
|  ___) | |   \ \/ / 
| |     | |____\  /  
|_|     |_______)/   
                     """)

time.sleep(5)
slow_type("\033[92m                     𝕄𝕒𝕕𝕖 𝕓𝕪: 𝕃𝕖𝔻𝕦𝕔𝔸𝕏", .03)
time.sleep(3)

url = "https://zefame.com/ref/kpjif"
title = "FLV"

set_console_title(title)
slow_type("L'URL va s'ouvrir dans 5 secondes...", .01)
time.sleep(5)
webbrowser.open(url)
