print("Count Down Timer")

import time

Utime = int(input("Enter time in seconds: "))

while Utime > 0:
    sec = int(Utime % 60)
    mins = int(Utime / 60 % 60)
    hours = int(Utime / 3600)
    print(f"{hours:02}:{mins:02}:{sec:02}")
    Utime -= 1
    time.sleep(1)
print("Time's up!")