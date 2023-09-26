# ALX System Engineering & DevOps - Web Server Configuration

This repository contains a series of tasks related to configuring a web server using Nginx, Puppet, and Bash scripts. The tasks are part of the ALX System Engineering & DevOps curriculum.

## Table of Contents

- [Project Overview](#project-overview)
- [Requirements](#requirements)
- [Tasks](#tasks)
  - [Task 0: Transfer a File to Your Server](#task-0-transfer-a-file-to-your-server)
  - [Task 1: Install Nginx Web Server](#task-1-install-nginx-web-server)
  - [Task 2: Setup a Domain Name](#task-2-setup-a-domain-name)
  - [Task 3: Redirection](#task-3-redirection)
  - [Task 4: Not Found Page 404](#task-4-not-found-page-404)
  - [Task 5: Install Nginx Web Server (with Puppet)](#task-5-install-nginx-web-server-with-puppet)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

In this project, you will learn how to configure a web server using various methods, including Bash scripts and Puppet manifests. The tasks cover the installation and configuration of Nginx, setting up domain names, handling redirection, customizing 404 error pages, and automating the configuration process.

## Requirements

Before you begin, make sure you have the following:

- A system running Ubuntu 16.04 LTS
- Access to the root user or a user with sudo privileges
- Basic knowledge of web servers and Linux system administration

## Tasks

### Task 0: Transfer a File to Your Server

- Write a Bash script that transfers a file from your client to a server.
- Accepts 4 parameters: the path to the file, server IP, username, and SSH private key.
- Display usage instructions if fewer than 3 parameters are provided.
- Use `scp` to transfer the file to the user's home directory on the server.
- Disable strict host key checking when using `scp`.

### Task 1: Install Nginx Web Server

- Write a Bash script that installs Nginx on your web server.
- Ensure that Nginx listens on port 80.
- Verify that querying Nginx at the root ("/") returns a page containing the string "Hello World!"
- Do not use `systemctl` for restarting Nginx.

### Task 2: Setup a Domain Name

- Provide a domain name (e.g., example.tech).
- Configure DNS records with an A entry to point to your web server's IP address.
- Add your domain name to the project website URL field.

### Task 3: Redirection

- Configure Nginx to perform a 301 Moved Permanently redirection for the "/redirect_me" location.
- Provide a Bash script to automatically configure a new Ubuntu machine with this redirection.

### Task 4: Not Found Page 404

- Configure Nginx to return an HTTP 404 error code with a custom 404 page containing the text "Ceci n'est pas une page."
- Provide a Bash script to automatically configure a new Ubuntu machine with this custom 404 page.

### Task 5: Install Nginx Web Server (with Puppet)

- Use Puppet to install and configure Nginx.
- Ensure Nginx listens on port 80.
- Verify that querying Nginx at the root ("/") returns a page containing the string "Hello World!"
- Implement a 301 Moved Permanently redirection for "/redirect_me" using Puppet resources.

## Usage

To complete each task, follow the instructions provided in the respective task files. You can use the Bash scripts and Puppet manifests provided to automate the configuration process.

## Contributing

Contributions to this project are welcome. If you find any issues or improvements, please open an issue or create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

