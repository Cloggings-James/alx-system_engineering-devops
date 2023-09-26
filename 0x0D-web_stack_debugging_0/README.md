**Project README: Web Stack Debugging #0**

### Introduction
This project is part of the Web Stack Debugging series, designed to train you in the art of debugging web applications. The series focuses on solving issues within broken or bugged web stacks, with the ultimate goal of creating a Bash script that can restore the web stack to a working state. This project, in particular, revolves around debugging a Docker container running an Apache web server.

### Background Context
Debugging is a crucial skill for Full-Stack Software Engineers, as computer systems and software often don't behave as expected. This project provides a hands-on opportunity to enhance your debugging skills by identifying and fixing issues in a web stack.

In this example, you'll be given a Docker container running an Ubuntu 14.04 image with Apache. The server should meet the following criteria:

1. Have a copy of the `/etc/passwd` file in `/tmp`.
2. Have a file named `/tmp/isworking` containing the string "OK."

Without these two elements, the web application on the server cannot function. Your task is to diagnose the problem and manually fix the server before creating a Bash script to automate the fix.

### Project Tasks
#### Task 0: Give me a page!
In this task, your objective is to get Apache to run within the Docker container and return a web page containing "Hello Holberton" when queried at the root URL.

**Example:**

```bash
docker run -p 8080:80 -d -it holbertonschool/265-0
```

After starting the Docker container, you might encounter an error message when querying the port 8080. Your mission is to connect to the container and fix the issue, ensuring that curling port 80 returns a page containing "Hello Holberton."

Please document the command(s) you used to fix the issue in your answer file.

### Requirements
#### General
- Allowed editors: vi, vim, emacs
- All your files will be interpreted on Ubuntu 14.04 LTS.
- All your files should end with a new line.
- A `README.md` file, at the root of the project folder, is mandatory.
- All your Bash script files must be executable.
- Your Bash scripts must pass Shellcheck without any errors.
- Your Bash scripts must run without error.
- The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`.
- The second line of all your Bash scripts should be a comment explaining what the script is doing.

### Concepts to Explore
- Network basics
- Docker
- Web stack debugging

### Resources
- `man` or `help`:
  - `curl`

### Deadline
- Project start: Sep 25, 2023, 6:00 AM
- Project end: Sep 27, 2023, 6:00 AM
- Checker release: Sep 26, 2023, 6:00 PM
- An auto-review will be launched at the deadline.

### Getting Help
If you encounter any issues or need assistance, please don't hesitate to seek help from your instructors, peers, or relevant online resources. Debugging is a collaborative effort, and there's a wealth of knowledge available to support you in this task.

Good luck with your debugging journey!
