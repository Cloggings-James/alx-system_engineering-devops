# HTTPS SSL Configuration Project

This project focuses on configuring HTTPS SSL for a web server, DNS setup, and creating a Bash script to query and display information about subdomains.

## Table of Contents

- [Project Overview](#project-overview)
- [Tasks](#tasks)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

In this project, we will configure HTTPS SSL for a web server using HAProxy, set up DNS records for subdomains, and create a Bash script to query and display information about these subdomains. The tasks include:

1. **World Wide Web**
   - Configure DNS records for subdomains (www, lb-01, web-01, web-02).
   - Create a Bash script to query and display DNS information for subdomains.

2. **HAProxy SSL Termination**
   - Configure HAProxy to accept and terminate SSL traffic for the www subdomain.
   - Ensure that accessing the root URL of the domain displays "Holberton School."

3. **No Loophole in Your Website Traffic (Advanced)**
   - Configure HAProxy to automatically redirect HTTP traffic to HTTPS.

## Tasks

- Task 0: DNS Configuration and Bash Script
- Task 1: HAProxy SSL Termination
- Task 2: Enforcing HTTPS Traffic (Advanced)

Each task comes with specific requirements and instructions, please refer to the individual task descriptions for more details.

## Getting Started

To get started with this project, make sure you have the following prerequisites:

- Access to a server or virtual machine running Ubuntu 16.04 LTS.
- DNS control panel access for your domain configuration.
- Basic knowledge of web servers, DNS, and Bash scripting.

## Usage

1. Clone this repository to your server:

```bash
git clone https://github.com/yourusername/https-ssl-project.git
cd https-ssl-project

