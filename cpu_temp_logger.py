"""
Copyright (c) [2024] Hiroshi. 
https:ww/iCyberia.com

License: [GNU General Public License]
You should have received a copy of the GNU General Public License

Purpose: Basic Python script that checks the CPU Temp with temp_str = os.popen('vcgencmd measure_temp').readline() and writes 
the current CPU temp to /temp.log with the time stamp. The length of the log file is also checked and once it reaches 1440 
lines the oldest line is removed. To edit this update this line: def manage_log_file(log_file, max_lines=1440):

Further documentation:
- https://github.com/iCyberia/Python-CPUTemp

Usage examples:
- Runs on Rapsberry Pi Zero W with Waveshare 3.7in E-Ink Display
"""


import os
from datetime import datetime

def get_cpu_temp():
    # Read the CPU temperature from the system file
    temp_str = os.popen('vcgencmd measure_temp').readline()
    # Extract the temperature value
    temp = float(temp_str.replace("temp=", "").replace("'C\n", ""))
    return temp

def get_cpu_voltage():
    # Read the CPU voltage from the system file
    voltage_str = os.popen('vcgencmd measure_volts').readline()
    # Extract the voltage value
    voltage = float(voltage_str.replace("volt=", "").replace("V\n", ""))
    return voltage

def log_temp_and_voltage_to_file(log_file):
    # Get the current CPU temperature and voltage
    cpu_temp = get_cpu_temp()
    cpu_voltage = get_cpu_voltage()
    # Get the current time and date
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Create the log entry
    log_entry = f"{current_time} - CPU Temp: {cpu_temp}°C - CPU Voltage: {cpu_voltage}V\n"
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
    log_temp_and_voltage_to_file(log_file_path)
    manage_log_file(log_file_path)
