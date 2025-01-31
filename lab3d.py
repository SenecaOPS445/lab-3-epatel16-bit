#!/usr/bin/env python3
# Author ID: epatel16

import subprocess

def free_space():
    # Run the 'df -h' command to get filesystem information
    p = subprocess.Popen(['df', '-h'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = p.communicate()
    
    # Error handling if the command fails
    if error:
        return f"Error: {error.decode('utf-8')}"
    
    # Filter for the root directory and return the available space
    for line in output.decode('utf-8').splitlines():
        if line.endswith('/'):
            # Splitting the line and selecting the available space column
            return line.split()[3].strip()

if __name__ == '__main__':
    print(free_space())

