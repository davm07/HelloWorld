# Hello World in Python
import time

def hello_countdown(seconds):
    for i in range(seconds, 0, -1):
        print(f"⌛ {i}...")
        time.sleep(1)
    print("🎉 Hello World!")

hello_countdown(3)