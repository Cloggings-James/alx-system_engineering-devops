# Project Title

## Overview

This project is a collection of tasks related to SSH and RSA key management for server administration. The tasks include creating SSH key pairs, configuring SSH clients, and connecting to remote hosts securely.

## Author

**Author:** James

## Table of Contents

- [Project Title](#project-title)
  - [Overview](#overview)
  - [Author](#author)
  - [Table of Contents](#table-of-contents)
  - [Tasks](#tasks)
    - [Task 0: Use a Private Key](#task-0-use-a-private-key)
    - [Task 1: Create an SSH Key Pair](#task-1-create-an-ssh-key-pair)
    - [Task 2: Client Configuration File](#task-2-client-configuration-file)
    - [Task 3: Let Me In!](#task-3-let-me-in)
    - [Task 4: Client Configuration File (w/ Puppet)](#task-4-client-configuration-file-w-puppet)
  - [Usage](#usage)
  - [Contributing](#contributing)
  - [License](#license)

## Tasks

### Task 0: Use a Private Key

- Write a Bash script to connect to a server using SSH with a private key.
- Usage: `./0-use_a_private_key`

### Task 1: Create an SSH Key Pair

- Write a Bash script to create an RSA key pair.
- Private key name: `school`
- Key bits: 4096
- Passphrase: betty

### Task 2: Client Configuration File

- Configure the SSH client to use the private key `~/.ssh/school`.
- Configure the SSH client to refuse password authentication.

### Task 3: Let Me In!

- Add an SSH public key to the server to allow access as the `ubuntu` user.

### Task 4: Client Configuration File (w/ Puppet)

- Use Puppet to configure the SSH client to use the private key `~/.ssh/school`.
- Configure Puppet to refuse password authentication.

## Usage

To use the scripts and configurations in this project, follow the instructions provided for each task in their respective directories.

## Contributing

Contributions are welcome! If you have improvements or additional tasks to add, please create a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

