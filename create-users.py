#!/usr/bin/python3

import os
import sys

# READ EACH LINE FROM STANDARD INPUT
for line in sys.stdin:

    line = line.strip()

    # Skip blank lines
    if len(line) == 0:
        continue

    # Skip comment lines that start with '#'
    if line[0] == '#':
        continue

    parts = line.split(':')

    # Check number of fields in line
    if len(parts) < 5:
        print("ERROR: Not enough parts in line:", line)
        continue

    username   = parts[0]
    password   = parts[1]
    lastname   = parts[2]
    firstname  = parts[3]
    group_list = parts[4]

    # Skip user if password is "-"
    if password == "-":
        print("SKIPPING USER:", username)
        continue

    # Build Linux user creation commands
    add_user_cmd = (
        "sudo adduser --disabled-password --gecos "
        f"'{firstname} {lastname}' {username}"
    )

    set_pw_cmd = f"echo '{username}:{password}' | sudo chpasswd"

    # Print commands that will run
    print(add_user_cmd)
    print(set_pw_cmd)

    # Execute commands
    os.system(add_user_cmd)
    os.system(set_pw_cmd)

    # Assign user to groups
    if group_list != "-":
        groups = group_list.split(',')
        for g in groups:
            group_cmd = f"sudo adduser {username} {g}"
            print(group_cmd)
            os.system(group_cmd)
