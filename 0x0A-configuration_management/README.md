# 0x0A. Configuration Management

This repository contains Puppet manifests for performing configuration management tasks. Below is a summary of the key tasks and their requirements:

### 0. Create a file

Using Puppet, a file is created at `/tmp` with the following attributes:

- File path is `/tmp/school`
- File permission is `0744`
- File owner is `www-data`
- File group is `www-data`
- File contains the text `I love Puppet`

### 1. Install a package

Puppet is used to install `puppet-lint` with version `2.5.0`.

### 2. Execute a command

Using Puppet, a manifest is created to kill a process named `killmenow`. This is achieved using the `exec` Puppet resource and the `pkill` command.

These tasks demonstrate the use of Puppet for configuration management, package installation, and executing commands to manage system configurations.

**Note:** All tasks are designed to work on an Ubuntu 20.04 LTS environment with Puppet 5.5 preinstalled. Additional instructions are provided for installing required packages (`puppet` and `puppet-lint`) if needed.

![Skynet](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2019/6/6a0a8024f2b1c47a9d1e.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20220311%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220311T121959Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=9ce50e87387c9b01da2af22461873db9083bc0b6e62ba9603674d6dd1abd3029)

**Resources:**

- [Intro to Configuration Management](https://alx-intranet.hbtn.io/rltoken/GL30hu-aRcKzPOvK8JO-Bg)
- [Puppet resource type: file](https://alx-intranet.hbtn.io/rltoken/DjSqEUZh5jSvzQbr8Hn_hA)
- [Puppet's Declarative Language: Modeling Instead of Scripting](https://alx-intranet.hbtn.io/rltoken/fZbIuIwhPZWQUQNTjsqu1A)
- [Puppet lint](https://alx-intranet.hbtn.io/rltoken/CRUMeEMdcX-UtbWsUM9xLQ)
- [Puppet emacs mode](https://alx-intranet.hbtn.io/rltoken/MzHXCntAkPzOqMnI6_rpWQ)
