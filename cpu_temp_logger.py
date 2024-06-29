import os
from datetime import datetime

def get_cpu_temp():
    # Read the CPU temperature from the system file
    temp_str = os.popen('vcgencmd measure_temp').readline()
    # Extract the temperature value
    temp = float(temp_str.replace("temp=", "").replace("'C\n", ""))
    return temp

def log_temp_to_file(log_file):
    # Get the current CPU temperature
    cpu_temp = get_cpu_temp()
    # Get the current time and date
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Create the log entry
    log_entry = f"{current_time} - CPU Temp: {cpu_temp}°C\n"
    # Write the log entry to the file
    with open(log_file, 'a') as file:
        file.write(log_entry)

def manage_log_file(log_file, max_lines=1440):
    # Read the log file and count the lines
    with open(log_file, 'r') as file:
        lines = file.readlines()
    
    # If the log file exceeds max_lines, remove the oldest line
    if len(lines) > max_lines:
        # Keep all lines except the oldest
        with open(log_file, 'w') as file:
            file.writelines(lines[1:])

if __name__ == "__main__":
    log_file_path = "/temp.log"
    log_temp_to_file(log_file_path)
    manage_log_file(log_file_path)
