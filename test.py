import time
timer = input("Enter your time in seconds: ")
for x in reversed(range(int(timer) + 1)):
    seconds = int(x) % 60
    minutes = (int(x) // 60) % 60
    hours = (int(x) // 3600) 
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
