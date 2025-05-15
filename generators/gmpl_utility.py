FILENAME = "dummy.txt"

def write_content_to_file(content):
    with open(FILENAME, 'a') as file:
        file.write(content)

def write_content_to_file_with_a_new_line(content):
    write_content_to_file(content + "\n")

def write_new_line_to_file():
    write_content_to_file_with_a_new_line("")

def clear_file():
    with open(FILENAME, 'w') as file:
        pass

def set_file_name(filename):
    global FILENAME 
    FILENAME = filename