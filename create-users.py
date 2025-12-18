#!/usr/bin/python3

# IMPORTS
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

    # check number of fields in the line
    if len(parts) < 5:
        print("ERROR: Not enough parts in line:", line)
        continue

    username = parts[0]
    password = parts[1]
    lastname = parts[2]
    firstname = parts[3]
    group_list = parts[4]

    # skip user if password is "-"
    if password == "-":
        print("SKIPPING USER:", username)
        continue

    # build Linux command strings
    add_user_cmd = "sudo adduser --disabled-password --gecos '" + firstname + " " + lastname + "' " + username
    set_pw_cmd = "echo '" + username + ":" + password + "' | sudo chpasswd"

    # Print the commands that WOULD run
    print(add_user_cmd)
    print(set_pw_cmd)

    # Actually run user creation commands
    # os.system(add_user_cmd)
    # os.system(set_pw_cmd)

    # If group list exists, process groups
    if group_list != "-":
        groups = group_list.split(',')
        for g in groups:
            group_cmd = "sudo adduser " + username + " " + g
            print(group_cmd)
            # os.system(group_cmd)
