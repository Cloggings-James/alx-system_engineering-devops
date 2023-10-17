# Web Stack Debugging #2

This project is part of the Alx System Engineering and DevOps curriculum. It focuses on debugging issues related to web servers, specifically Nginx configuration.

## Task 0: Run software as another user

In this task, a Bash script (`0-iamsomeoneelse`) is provided that accepts a username as an argument and runs the `whoami` command as that user. This demonstrates how to execute commands as another user.

Usage:
```bash
./0-iamsomeoneelse [username]
Task 1: Run Nginx as Nginx
The goal of this task is to configure Nginx to run as the less privileged nginx user instead of the root user. This enhances security by limiting the impact of a security breach.

To run the script:

bash
Copy code
./1-run_nginx_as_nginx
Task 2: 7 lines or less
This advanced task requires you to make the Nginx user configuration script from Task 1 even more concise. The new script should be 7 lines or fewer.

Requirements
All scripts should be executable.
Scripts must pass Shellcheck without errors.
The first line of each Bash script should be #!/usr/bin/env bash.
Each script should include a comment explaining its purpose.
You cannot use ;, &&, or wget in Task 2.
Author
Clogging-James
Acknowledgments
Special thanks to the Alx System Engineering and DevOps team.
