# 0x15. API

## Overview

This project focuses on utilizing Python to work with REST APIs. It's designed to demonstrate how to gather data from an API, format it, and export it to different data structures like CSV and JSON. The project promotes good coding practices and adherence to the Python PEP8 style guide.

The project consists of three tasks, each building upon the previous one:

1. **Gather data from an API**: A Python script that retrieves information about an employee's TODO list progress from a REST API. It displays the progress and list of tasks.

2. **Export to CSV**: Extends the previous script to export data in CSV format. It records tasks owned by an employee in a CSV file with a specific format.

3. **Export to JSON**: Further extends the initial script to export data in JSON format, recording tasks in a JSON file.

## Learning Objectives

- Understand the limitations of Bash scripting and when to use Python.
- Gain knowledge about APIs, REST APIs, and microservices.
- Learn about data formats such as CSV and JSON.
- Apply Pythonic coding style guidelines and follow best practices.

## Requirements

- Editors allowed: vi, vim, emacs.
- All scripts should be interpreted on Ubuntu 20.04 LTS using Python 3.8.5.
- Files should end with a new line.
- All scripts should start with `#!/usr/bin/python3`.
- Libraries should be organized alphabetically.
- Code must be PEP8 compliant (using pycodestyle).
- README.md file at the project root.
- All scripts must be executable.
- Modules should have documentation.
- Use 'get' to access dictionary values to avoid exceptions.
- Avoid code execution when imported using `if __name__ == "__main__":`.

## Tasks

### 0. Gather data from an API

This task involves creating a Python script that fetches employee TODO list progress from a REST API. It takes an employee ID as a parameter and displays the progress in a specific format.

Example:

```sh
$ python3 0-gather_data_from_an_API.py 2
Employee Ervin Howell is done with tasks(8/20):
     distinctio vitae autem nihil ut molestias quo
     voluptas quo tenetur perspiciatis explicabo natus
     ...
$ python3 1-export_to_CSV.py 2
$ cat 2.csv
"2","Antonette","False","suscipit repellat esse quibusdam voluptatem incidunt"
"2","Antonette","True","distinctio vitae autem nihil ut molestias quo"
...
$ python3 2-export_to_JSON.py 2
$ cat 2.json
{"2": [{"task": "suscipit repellat esse quibusdam voluptatem incidunt", "completed": false, "username": "Antonette"}, {"task": "distinctio vitae autem nihil ut molestias quo", "completed": true, "username": "Antonette"}, ...]}

