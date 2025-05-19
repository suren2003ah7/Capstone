import gmpl_utility as util
import random

FILENAME = "timetable.txt"
OFFICES = 18
PROFESSORS = 35
HOURS = 8

professorRequiredWorkHours = []

def generate_x_variables():
    util.write_content_to_file_with_a_new_line("# x variables")
    for i in range(1, OFFICES + 1):
        for j in range(1, PROFESSORS + 1):
            for k in range(1, HOURS + 1):
                term = f"x_{i}_{j}_{k}"
                content = "var " + term + " binary;"
                util.write_content_to_file_with_a_new_line(content)
    util.write_new_line_to_file()

def generate_y_variables():
    util.write_content_to_file_with_a_new_line("# y variables")
    for i in range(1, OFFICES + 1):
        for j in range(1, PROFESSORS + 1):
            for k in range(1, HOURS + 1):
                term = f"y_{i}_{j}_{k}"
                content = "var " + term + " binary;"
                util.write_content_to_file_with_a_new_line(content)
    util.write_new_line_to_file()

def generate_a_variables():
    util.write_content_to_file_with_a_new_line("# a variables")
    for i in range(1, OFFICES + 1):
        for j in range(1, PROFESSORS + 1):
            for k in range(1, HOURS):
                term = f"a_{i}_{j}_{k}"
                content = "var " + term + " binary;"
                util.write_content_to_file_with_a_new_line(content)
    util.write_new_line_to_file()

def generate_z_variables():
    util.write_content_to_file_with_a_new_line("# z variables")
    for i in range(1, OFFICES + 1):
        for j in range(1, PROFESSORS + 1):
            term = f"z_{i}_{j}"
            content = "var " + term + " integer >= 0;"
            util.write_content_to_file_with_a_new_line(content)
    util.write_new_line_to_file()

def generate_objective_function():
    util.write_content_to_file_with_a_new_line("# Objective function")
    util.write_content_to_file_with_a_new_line("maximize z:")
    for i in range(1, PROFESSORS + 1):
        m = 2**(PROFESSORS - i + 1)
        util.write_content_to_file(f"{m} * (")
        for j in range(1, OFFICES + 1):
            for k in range(1, HOURS + 1):
                if k == HOURS and j == OFFICES:
                    term = f"y_{j}_{i}_{k}"
                else:
                    term = f"y_{j}_{i}_{k} + "
                util.write_content_to_file(term)
        util.write_content_to_file_with_a_new_line(") +")
    for i in range(1, OFFICES + 1):
        for j in range(1, PROFESSORS + 1):
            if j == PROFESSORS and i == OFFICES:
                term = f"z_{i}_{j}"
            else:
                term = f"z_{i}_{j} + "
            util.write_content_to_file(term)
    util.write_content_to_file_with_a_new_line(";")
    util.write_new_line_to_file()

def generate_x_y_matching_constraints():
    util.write_content_to_file_with_a_new_line("# Matching x and y")
    for i in range(1, OFFICES + 1):
        for j in range(1, HOURS + 1):
            util.write_content_to_file_with_a_new_line(f"subject to match_y_{i}_X_{j}:")
            for k in range(1, PROFESSORS + 1):
                if k == PROFESSORS:
                    term = f"x_{i}_{k}_{j} = "
                else:
                    term = f"x_{i}_{k}_{j} + "
                util.write_content_to_file(term)
            for k in range(1, PROFESSORS + 1):
                if k == PROFESSORS:
                    term = f"y_{i}_{k}_{j};"
                else:
                    term = f"y_{i}_{k}_{j} + "
                util.write_content_to_file(term)
            util.write_new_line_to_file()
    util.write_new_line_to_file()

def generate_x_sum_constraints():
    util.write_content_to_file_with_a_new_line("# Sum constraints for x")
    for i in range(1, PROFESSORS + 1):
        util.write_content_to_file_with_a_new_line(f"subject to sum_x_X_{i}_X:")
        for j in range(1, OFFICES + 1):
            for k in range(1, HOURS + 1):
                if j == OFFICES and k == HOURS:
                    term = f"x_{j}_{i}_{k} = "
                else:
                    term = f"x_{j}_{i}_{k} + "
                util.write_content_to_file(term)
        util.write_content_to_file_with_a_new_line(f"{professorRequiredWorkHours[i - 1]};")
    util.write_new_line_to_file()

def generate_professor_placement_constraints():
    util.write_content_to_file_with_a_new_line("# Professor placement constraints")
    for j in range(1, PROFESSORS + 1):
        for k in range(1, HOURS + 1):
            util.write_content_to_file_with_a_new_line(f"subject to placement_professor_{j}_hour_{k}:")
            for i in range(1, OFFICES + 1):
                if i == OFFICES:
                    term = f"x_{i}_{j}_{k} <= 1;"
                else:
                    term = f"x_{i}_{j}_{k} + "
                util.write_content_to_file(term)
            util.write_new_line_to_file()
    util.write_new_line_to_file()


def generate_z_constraints():
    util.write_content_to_file_with_a_new_line("# z constraints")
    for i in range(1, OFFICES + 1):
        for j in range(1, PROFESSORS + 1):
            util.write_content_to_file_with_a_new_line(f"subject to sum_z_{i}_{j}:")
            util.write_content_to_file(f"z_{i}_{j} = ")
            for k in range(1, HOURS):
                if k == HOURS - 1:
                    term = f"a_{i}_{j}_{k};"
                else:
                    term = f"a_{i}_{j}_{k} + "
                util.write_content_to_file(term)
            util.write_new_line_to_file()
    util.write_new_line_to_file()

def generate_a_constraints():
    util.write_content_to_file_with_a_new_line("# a constraints")
    for i in range(1, OFFICES + 1):
        for j in range(1, PROFESSORS + 1):
            for k in range(1, HOURS):
                util.write_content_to_file(f"subject to a_{i}_{j}_{k}_dependency_1: ")
                util.write_content_to_file_with_a_new_line(f"a_{i}_{j}_{k} <= x_{i}_{j}_{k};")
                util.write_content_to_file(f"subject to a_{i}_{j}_{k}_dependency_2: ")
                util.write_content_to_file_with_a_new_line(f"a_{i}_{j}_{k} <= x_{i}_{j}_{k + 1};")
                util.write_content_to_file(f"subject to a_{i}_{j}_{k}_dependency_3: ")
                util.write_content_to_file_with_a_new_line(f"a_{i}_{j}_{k} >= x_{i}_{j}_{k} + x_{i}_{j}_{k + 1} - 1;")
                util.write_new_line_to_file()
    util.write_new_line_to_file()

def generate_y_constraints():
    util.write_content_to_file_with_a_new_line("# y constraints")
    for i in range(1, OFFICES + 1):
        for j in range(2, PROFESSORS + 1):
            for k in range(1, HOURS + 1):
                term = f"y_{i}_{j}_{k}"
                for k2 in range(1, HOURS + 1):
                    util.write_content_to_file(f"subject to {term}_dependency_{k2}: ")
                    util.write_content_to_file_with_a_new_line(f"{term} <= y_{i}_{j - 1}_{k2};")
                util.write_new_line_to_file()
    util.write_new_line_to_file()
                
util.set_file_name(FILENAME)
util.clear_file()

for _ in range(PROFESSORS):
    professorRequiredWorkHours.append(random.randint(1, 8))
print("Preprocessing Complete!")

generate_x_variables()
print("x variables generated")

generate_y_variables()
print("y variables generated")

generate_a_variables()
print("a variables generated")

generate_z_variables()
print("z variables generated")

generate_objective_function()
print("Objective function generated")

generate_x_y_matching_constraints()
print("x and y matching constraints generated")

generate_x_sum_constraints()
print("x sum constraints generated")

generate_professor_placement_constraints()
print("professor placement constraints generated")

generate_z_constraints()
print("z constraints generated")

generate_a_constraints()
print("a constraints generated")

generate_y_constraints()
print("y constraints generated")

print("Done!")
