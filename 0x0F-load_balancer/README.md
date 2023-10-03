# Project: Load Balancer Setup with HAproxy

This project involves setting up a load balancer and configuring web servers on Ubuntu servers to enhance redundancy and improve infrastructure reliability. The tasks involve automating various configurations using Bash scripts and Puppet.

## Table of Contents
- [Tasks](#tasks)
  - [Task 0: Double the number of webservers](#task-0-double-the-number-of-webservers)
  - [Task 1: Install your load balancer](#task-1-install-your-load-balancer)
  - [Task 2: Add a custom HTTP header with Puppet (Advanced)](#task-2-add-a-custom-http-header-with-puppet-advanced)
- [Requirements](#requirements)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Tasks

### Task 0: Double the number of webservers

In this task, you need to configure web-02 to be identical to web-01 and add a custom Nginx response header named `X-Served-By`. This header should contain the hostname of the server running Nginx. You will need to write a Bash script (`0-custom_http_response_header.sh`) to automate this configuration.

### Task 1: Install your load balancer

In this task, you must install and configure HAproxy on your lb-01 server. HAproxy should be set up to send traffic to both web-01 and web-02 using a round-robin algorithm. Additionally, you need to ensure that HAproxy can be managed via an init script. You should also make sure that your servers have the right hostnames: `[STUDENT_ID]-web-01` and `[STUDENT_ID]-web-02`. You will need to write a Bash script (`1-install_load_balancer.sh`) to automate this setup.

### Task 2: Add a custom HTTP header with Puppet (Advanced)

This advanced task requires you to automate the process of creating a custom HTTP header response with Puppet. You should create a custom header named `X-Served-By` with the value being the hostname of the server running Nginx. You will need to write a Puppet manifest file (`2-puppet_custom_http_response_header.pp`) to automate this configuration.

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted on Ubuntu 16.04 LTS
- All your files should end with a new line
- A README.md file, at the root of the folder of the project, is mandatory
- All your Bash script files must be executable
- Your Bash script must pass Shellcheck (version 0.3.7) without any error
- The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all your Bash scripts should be a comment explaining what the script is doing

## Project Structure


