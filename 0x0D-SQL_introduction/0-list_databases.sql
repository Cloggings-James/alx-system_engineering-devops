#!/bin/bash

# MySQL server details
MYSQL_HOST="localhost"
MYSQL_USER="root"
MYSQL_PASSWORD="12345204001"  # 

# Command to list databases
MYSQL_COMMAND="mysql -h$MYSQL_HOST -u$MYSQL_USER -p$MYSQL_PASSWORD -e 'SHOW DATABASES;'"

# Execute the command and display databases
$MYSQL_COMMAND

