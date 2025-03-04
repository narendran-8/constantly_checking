import time
from datetime import datetime

FILE_PATH = "time.txt"



# connection , data need, format , input to this

# Function to call when time matches
def hello_world():
    print("Hello, World!")

# Function to read ID, time, and status from file
def read_data_from_file(file_path=FILE_PATH):
    try:
        with open(file_path, "r") as file:
            data = file.read().strip()
            if not data:
                return None  # Return None if file is empty

            parts = data.split(",")  # Split by comma
            if len(parts) != 3:
                print("Invalid file format. Expected: ID,Time,Status")
                return None
           
            unique_id, file_time, status = parts[0].strip(), parts[1].strip(), parts[2].strip().lower()
            status = status == "true"  # Convert to boolean
            return unique_id, file_time, status
    except FileNotFoundError:
        print("File not found, waiting for file...")
        return None

# Function to update status in file
def update_status_in_file(file_path=FILE_PATH):
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
       
        if lines:
            parts = lines[0].strip().split(",")
            if len(parts) == 3:
                parts[2] = "True"  # Update status to True
                new_content = ",".join(parts)

                with open(file_path, "w") as file:
                    file.write(new_content)
    except Exception as e:
        print(f"Error updating file: {e}")

# Function to constantly check time
def monitor_time():
    while True:
        data = read_data_from_file()
       
        if data:
            unique_id, file_time, status = data
           
            if not status:  # Run only if status is False
                try:
                    file_time_obj = datetime.strptime(file_time, "%I.%M %p").time()
                    current_time = datetime.now().time().replace(second=0, microsecond=0)

                    if current_time == file_time_obj:
                        print(f"ID: {unique_id} - Time Matched: {file_time}")
                        hello_world()
                        update_status_in_file()  # Update status to True
                except ValueError:
                    print("Invalid time format in file. Use format: ID,HH.MM AM/PM,Status")
       
        time.sleep(1)  # Check every 1 seconds

# Start monitoring
monitor_time()


