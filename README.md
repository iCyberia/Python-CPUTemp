# Python-CPUTemp
Basic Python script that checks the CPU Temp with temp_str = os.popen('vcgencmd measure_temp').readline() and writes the current CPU temp to /temp.log with the time stamp.
The length of the log file is also checked and once it reaches 1440 lines the oldest line is removed. 


## Install
Clone the git with the command line:
```
git clone https://github.com/iCyberia/Python-CPUTemp
```

Run with cron by using `Sudo crontab -e` and add
```
* * * * * python /cpu_temp_logger.py
```

## Check the log
```
tail temp.log
```


### Customize
The log file will grow to an overwelming size if left for weeks and weeks on end. I've set a limit of 1440 (1 per minute  = 24hrs)
To edit this update this line: 
```
def manage_log_file(log_file, max_lines=1440):
```




### Example Output:
```
2024-06-30 01:25:27 - CPU Temp: 45.1°C - CPU Voltage: 1.2563V
2024-06-30 01:26:02 - CPU Temp: 45.6°C - CPU Voltage: 1.2563V
2024-06-30 01:27:01 - CPU Temp: 45.1°C - CPU Voltage: 1.2563V
2024-06-30 01:28:01 - CPU Temp: 45.1°C - CPU Voltage: 1.2563V
2024-06-30 01:29:01 - CPU Temp: 45.6°C - CPU Voltage: 1.2563V
2024-06-30 01:30:01 - CPU Temp: 45.1°C - CPU Voltage: 1.2563V
2024-06-30 01:31:01 - CPU Temp: 45.1°C - CPU Voltage: 1.2563V
2024-06-30 01:32:01 - CPU Temp: 45.1°C - CPU Voltage: 1.2563V
```
