import time

print("Stopwatch started. Press Ctrl+C to stop.\n")
start_time = time.time()

try:
    while True:
        elapsed = time.time() - start_time
        mins = int(elapsed // 60)
        secs = int(elapsed % 60)
        print(f"\rTime: {mins:02d}:{secs:02d}", end="")
        time.sleep(1)
except KeyboardInterrupt:
    print(f"\n\nFinal time: {mins:02d}:{secs:02d}")

