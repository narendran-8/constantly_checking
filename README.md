# Time-Based Task Scheduler

This Python script monitors a `time.txt` file and executes a function when the current system time matches the scheduled time. It updates the file to prevent repeated execution.

## Features
- Reads an external file (`time.txt`) containing:

- Checks the current system time every second.
- Executes `hello_world()` when the time matches.
- Updates the file status to `True` to prevent re-execution.

## Prerequisites
- Python 3.x

## Installation
Clone this repository:
```bash
git clone https://github.com/your-username/your-repository.git
cd your-repository
```


## Usage
- Create a ```time.txt``` file with the following format:
- ```bash
    1234,10.30 AM,False
  ```
- Set the desired execution time in ``` HH.MM AM/PM``` format.
- Set `False` as the initial status..

