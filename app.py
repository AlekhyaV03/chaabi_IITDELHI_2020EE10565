import subprocess

# subprocess.run(['python', 'C:\\Users\KARRI LAKSHMI YAMINI\OneDrive - IIT Delhi\Desktop\yamini\hello.py'])
# main.py
# main.py

# main.py

import subprocess
import os

def run_subprocess_with_input(input_str):
    # Get the full path to other_file.py
    current_directory = os.path.dirname(os.path.abspath(__file__))
    other_file_path = os.path.join(current_directory, 'out.py')

    # The command to run the other Python script
    command = ['python', other_file_path]

    # Start the subprocess and connect to its input and output
    process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Send input and get the output
    output, error = process.communicate(input=input_str)

    if error:
        print(f"Error: {error}")
    else:
        return output.strip()

# Loop to continuously ask for input and print the response

# user_input = "healthy snacks"

# response = run_subprocess_with_input(user_input) print(f"Response from other_file.py: {response}")

user_input = input("Enter something (or 'ctrl+c' to exit): ")

output = run_subprocess_with_input(user_input)
print(output)