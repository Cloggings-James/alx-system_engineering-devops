# Firewall Project

**Author:** [Your Name]

## Overview

This project involves setting up a firewall and configuring port forwarding on a Linux server. The tasks include blocking incoming traffic on specific ports and forwarding traffic from one port to another.

## Table of Contents

1. [Task 0: Block all incoming traffic](#task-0-block-all-incoming-traffic)
2. [Task 1: Port forwarding](#task-1-port-forwarding)

## Task 0: Block all incoming traffic

In this task, we configure the `ufw` (Uncomplicated Firewall) to block all incoming traffic on a server except for specific TCP ports. The allowed ports are SSH (22), HTTPS SSL (443), and HTTP (80).

### Instructions

To complete this task, follow these steps:

1. Install `ufw` if not already installed.
2. Configure `ufw` to allow only SSH, HTTPS, and HTTP traffic.
3. Share the `ufw` commands used in your answer file.

## Task 1: Port forwarding

In this advanced task, we configure port forwarding on the server to redirect incoming traffic from port 8080 to port 80. This can be useful for routing external traffic to specific services.

### Instructions

To complete this task, follow these steps:

1. Modify the `ufw` configuration file to set up port forwarding.
2. Test the port forwarding to ensure it redirects traffic correctly.
3. Share a copy of the `ufw` configuration file you modified in your answer file.

## Usage

You can execute the provided commands on the specified servers to complete the tasks. Ensure you follow best practices when configuring the firewall to prevent any unintended issues.

## Author

[Your Name] - [GitHub Profile](https://github.com/yourusername)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

