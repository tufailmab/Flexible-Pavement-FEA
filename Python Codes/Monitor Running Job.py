# For Job Monitering, you need this code to use:
import os
import time

class StaFileMonitor:
    def __init__(self, filename):
        self.filename = filename
        self.last_position = 0
        self.last_line = ""

    def update_last_line(self):
        try:
            with open(self.filename, 'r') as file:
                file.seek(self.last_position)
                lines = file.readlines()
                if lines:
                    self.last_position = file.tell()
                    new_last_line = lines[-1].strip()
                    if new_last_line != self.last_line:
                        self.last_line = new_last_line
                        print(f"Job Status Update: {self.last_line}")
        except FileNotFoundError:
            print(f"File {self.filename} not found.")

def wait_for_sta_file():
    print("Scanning the directory for .sta file... \nPatience, the hunt is on!")
    while True:
        sta_file = find_sta_file()
        if sta_file:
            print(f"\nFound .sta file: {sta_file}\n")
            return sta_file
        time.sleep(1)

def find_sta_file():
    for filename in os.listdir('.'):
        if filename.endswith('.sta'):
            return filename
    return None

def main():
    # Look for the .sta file
    sta_file = wait_for_sta_file()
    
    print("Now monitoring job status in real-time.\nPress Ctrl+C to stop.")

    monitor = StaFileMonitor(sta_file)

    try:
        while True:
            monitor.update_last_line()
            time.sleep(1)  # Check for updates every second
    except KeyboardInterrupt:
        print("\nMonitoring stopped. Goodbye!")

if __name__ == "__main__":
    main()
