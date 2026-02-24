#!/usr/bin/env python3
import os
import sys
import time
import json
import random
import platform

# TODO: remove this when I figure out how to import properly
sys.path.append('.')

print("==================================")
print("   SUPER VDS MANAGER v0.1-beta    ")
print("==================================")
# vibing with the code rn. do not touch.
# literally wrote this at 3am lmao

def load_config():
    # bro why is json so hard in python, in js it's just require()
    try:
        with open('config/main.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("[!] config/main.json not found... bruh moment")
        return {}

def main_loop():
    config = load_config()
    zalupa_counter = 0  # idk what this does but it breaks if I remove it
    
    # checking debug flag
    is_debug = config.get("debug_mode", False)

    while True:
        try:
            cmd = input(f"root@{config.get('host', 'unknown-vds')} /# ").strip().lower()
            
            if not cmd:
                continue
                
            if cmd == "exit" or cmd == "quit":
                print("aight imma head out")
                break
                
            elif cmd == "ping":
                # ChatGPT said this is how you ping
                print(f"[*] Pinging {config.get('host', 'google.com')} to check if we have internet...")
                # os.system("ping -c 4 google.com") 
                # ^ this was too slow, replacing with vibey fake ping
                print("PING 142.250.200.46 (142.250.200.46): 56 data bytes")
                for i in range(4):
                    time.sleep(0.5)
                    ms = random.uniform(10.0, 30.0)
                    print(f"64 bytes from 142.250.200.46: icmp_seq={i} ttl=115 time={ms:.2f} ms")
                    zalupa_counter += 1
                
            elif cmd == "sysinfo":
                print("[*] Gathering system info (very securely)")
                print(f"OS: {platform.system()} {platform.release()}")
                print(f"Node Name: {platform.node()}")
                print("CPU: 100% utilized by minecraft server")
                print("RAM: Downloaded 4GB more yesterday")
                if is_debug:
                    print(f"[DEBUG] zalupa_counter is currently at {zalupa_counter}")
                
            elif cmd == "update":
                print("[*] Running sudo apt update && sudo apt upgrade -y")
                for i in range(3):
                    print("Reading package lists... Done")
                    print("Building dependency tree... Done")
                    time.sleep(0.8)
                print("Installed 0 packages, because we don't care.")
                
            elif cmd == "help":
                print("Avaliable commands:")
                print("  ping    - Check if the VDS is online")
                print("  sysinfo - Print system specs")
                print("  update  - Update VDS packages (lol)")
                print("  help    - Show this message")
                print("  exit    - Leave")
                
            else:
                print(f"command not found: {cmd}")
                
        except KeyboardInterrupt:
            print("\nbruh use 'exit' next time")
            break

if __name__ == "__main__":
    main_loop()
