def write_file(file_name, file_content):
    # Add .txt file extension to the file_name
    file_name = str(file_name) + ".txt"
    
    # Write the file_content to the specified file_name
    with open(file_name, 'w') as file:
        file.write(file_content)
def append_file(file_name, append_content):
    # Add .txt file extension to the file_name
    file_name = str(file_name) + ".txt"
    
    # Append the append_content to the specified file_name
    with open(file_name, 'a') as file:
        file.write(append_content)

def read_file(file_name):
    # Add .txt file extension to the file_name
    file_name = str(file_name) + ".txt"
    
    # Read the content of the specified file_name and return it
    with open(file_name, 'r') as file:
        return file.read()
