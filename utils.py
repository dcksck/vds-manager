import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_current_time():
    return time.strftime("%Y-%m-%d %H:%M:%S")

def fake_loading_bar(total_len=20):
    print("[", end="", flush=True)
    for _ in range(total_len):
        print("=", end="", flush=True)
        time.sleep(0.05)
    print("] DONE")
