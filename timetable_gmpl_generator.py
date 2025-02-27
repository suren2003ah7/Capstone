FILENAME = "command.txt"
OFFICES = 2
PROFESSORS = 5
HOURS = 8

professorRequiredWorkHours = [7,8,7,8,7]

def write_content_to_file(content):
    with open(FILENAME, 'a') as file:
        file.write(content)

def write_content_to_file_with_a_new_line(content):
    with open(FILENAME, 'a') as file:
        file.write(content + "\n")

def clear_file():
    with open(FILENAME, 'w') as file:
        pass

def generate_x_variables():
    write_content_to_file_with_a_new_line("# x variables")
    for i in range(1, OFFICES + 1):
        for j in range(1, PROFESSORS + 1):
            for k in range(1, HOURS + 1):
                term = f"x_{i}_{j}_{k}"
                content = "var " + term + " binary;"
                write_content_to_file_with_a_new_line(content)
    write_content_to_file_with_a_new_line("")

def generate_y_variables():
    write_content_to_file_with_a_new_line("# y variables")
    for i in range(1, OFFICES + 1):
        for j in range(1, PROFESSORS + 1):
            for k in range(1, HOURS + 1):
                term = f"y_{i}_{j}_{k}"
                content = "var " + term + " binary;"
                write_content_to_file_with_a_new_line(content)
    write_content_to_file_with_a_new_line("")

def generate_a_variables():
    write_content_to_file_with_a_new_line("# a variables")
    for i in range(1, OFFICES + 1):
        for j in range(1, PROFESSORS + 1):
            for k in range(1, HOURS):
                term = f"a_{i}_{j}_{k}"
                content = "var " + term + " binary;"
                write_content_to_file_with_a_new_line(content)
    write_content_to_file_with_a_new_line("")

def generate_z_variables():
    write_content_to_file_with_a_new_line("# z variables")
    for i in range(1, OFFICES + 1):
        for j in range(1, PROFESSORS + 1):
            term = f"z_{i}_{j}"
            content = "var " + term + " integer >= 0;"
            write_content_to_file_with_a_new_line(content)
    write_content_to_file_with_a_new_line("")

def generate_objective_function():
    write_content_to_file_with_a_new_line("# Objective function")
    write_content_to_file_with_a_new_line("maximize z:")
    for i in range(1, PROFESSORS + 1):
        m = 2**(PROFESSORS - i + 1)
        write_content_to_file(f"{m} * (")
        for j in range(1, OFFICES + 1):
            for k in range(1, HOURS + 1):
                if k == HOURS and j == OFFICES:
                    term = f"y_{j}_{i}_{k}"
                else:
                    term = f"y_{j}_{i}_{k} + "
                write_content_to_file(term)
        write_content_to_file_with_a_new_line(") +")
    for i in range(1, OFFICES + 1):
        for j in range(1, PROFESSORS + 1):
            if j == PROFESSORS and i == OFFICES:
                term = f"z_{i}_{j}"
            else:
                term = f"z_{i}_{j} + "
            write_content_to_file(term)
    write_content_to_file_with_a_new_line(";")
    write_content_to_file_with_a_new_line("")

def generate_x_y_matching_constraints():
    write_content_to_file_with_a_new_line("# Matching x and y")
    for i in range(1, OFFICES + 1):
        for j in range(1, HOURS + 1):
            write_content_to_file_with_a_new_line(f"subject to match_y_{i}_X_{j}:")
            for k in range(1, PROFESSORS + 1):
                if k == PROFESSORS:
                    term = f"x_{i}_{k}_{j} = "
                else:
                    term = f"x_{i}_{k}_{j} + "
                write_content_to_file(term)
            for k in range(1, PROFESSORS + 1):
                if k == PROFESSORS:
                    term = f"y_{i}_{k}_{j};"
                else:
                    term = f"y_{i}_{k}_{j} + "
                write_content_to_file(term)
            write_content_to_file_with_a_new_line("")
    write_content_to_file_with_a_new_line("")

def generate_x_sum_constraints():
    write_content_to_file_with_a_new_line("# Sum constraints for x")
    for i in range(1, PROFESSORS + 1):
        write_content_to_file_with_a_new_line(f"subject to sum_x_X_{i}_X:")
        for j in range(1, OFFICES + 1):
            for k in range(1, HOURS + 1):
                if j == OFFICES and k == HOURS:
                    term = f"x_{j}_{i}_{k} = "
                else:
                    term = f"x_{j}_{i}_{k} + "
                write_content_to_file(term)
        write_content_to_file_with_a_new_line(f"{professorRequiredWorkHours[i - 1]};")
    write_content_to_file_with_a_new_line("")

def generate_z_constraints():
    write_content_to_file_with_a_new_line("# z constraints")
    for i in range(1, OFFICES + 1):
        for j in range(1, PROFESSORS + 1):
            write_content_to_file_with_a_new_line(f"subject to sum_z_{i}_{j}:")
            write_content_to_file(f"z_{i}_{j} = ")
            for k in range(1, HOURS):
                if k == HOURS - 1:
                    term = f"a_{i}_{j}_{k};"
                else:
                    term = f"a_{i}_{j}_{k} + "
                write_content_to_file(term)
            write_content_to_file_with_a_new_line("")
    write_content_to_file_with_a_new_line("")

def generate_a_constraints():
    write_content_to_file_with_a_new_line("# a constraints")
    for i in range(1, OFFICES + 1):
        for j in range(1, PROFESSORS + 1):
            for k in range(1, HOURS):
                write_content_to_file(f"subject to a_{i}_{j}_{k}_dependency_1: ")
                write_content_to_file_with_a_new_line(f"a_{i}_{j}_{k} <= x_{i}_{j}_{k};")
                write_content_to_file(f"subject to a_{i}_{j}_{k}_dependency_2: ")
                write_content_to_file_with_a_new_line(f"a_{i}_{j}_{k} <= x_{i}_{j}_{k + 1};")
                write_content_to_file(f"subject to a_{i}_{j}_{k}_dependency_3: ")
                write_content_to_file_with_a_new_line(f"a_{i}_{j}_{k} >= x_{i}_{j}_{k} + x_{i}_{j}_{k + 1} - 1;")
                write_content_to_file_with_a_new_line("")
    write_content_to_file_with_a_new_line("")

def generate_y_constraints():
    write_content_to_file_with_a_new_line("# y constraints")
    for i in range(1, OFFICES + 1):
        for j in range(2, PROFESSORS + 1):
            for k in range(1, HOURS + 1):
                term = f"y_{i}_{j}_{k}"
                for k2 in range(1, HOURS + 1):
                    write_content_to_file(f"subject to {term}_dependency_{k2}: ")
                    write_content_to_file_with_a_new_line(f"{term} <= y_{i}_{j - 1}_{k2};")
                write_content_to_file_with_a_new_line("")
    write_content_to_file_with_a_new_line("")
                
clear_file()

generate_x_variables()
generate_y_variables()
generate_a_variables()
generate_z_variables()

generate_objective_function()

generate_x_y_matching_constraints()
generate_x_sum_constraints()
generate_z_constraints()
generate_a_constraints()
generate_y_constraints()
