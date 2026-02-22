import time
import random

while True:
    input("Press Enter to start...")
    wait = random.randint(2, 5)
    time.sleep(wait)
    start = time.time()
    input("NOW! Press Enter as fast as you can!")
    end = time.time()

    print("Your reaction time:", round(end - start, 3), "seconds")

