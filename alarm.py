import time

# Ask user for amount of time to wait
# initiate timer
# stop timer once time asked by the user has elapsed
# maybe play an audio file to let the user know time has elapsed

period = int(input("Enter time to wait in seconds: "))

start_time = time.time()

while True:
    current_time = time.time()
    time.sleep(0.1)
    elapsed_time = current_time - start_time

    if elapsed_time >= period:
        print("Time's up!")
        break
