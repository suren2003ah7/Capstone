import gmpl_utility as util

FILENAME = "pickup.txt"
DELIVERY_BOYS = 2
CUSTOMERS = 3

WAIT_TIME_COEFFICIENTS = [30, 60, 15]
M = 0
for c in WAIT_TIME_COEFFICIENTS:
    M += c

def generate_t_variables():
    util.write_content_to_file_with_a_new_line("# t variables")
    for k in range(1, CUSTOMERS + 1):
        util.write_content_to_file_with_a_new_line(f"var t_{k} integer >= 0;")
    util.write_new_line_to_file()

def generate_y_variables():
    util.write_content_to_file_with_a_new_line("# y variables")
    for i in range(1, DELIVERY_BOYS + 1):
        for j in range(1, CUSTOMERS + 1):
            for k in range(1, CUSTOMERS + 1):
                util.write_content_to_file_with_a_new_line(f"var y_{i}_{j}_{k} binary;")
    util.write_new_line_to_file()

def generate_objective_function():
    util.write_content_to_file_with_a_new_line("# objective function")
    util.write_content_to_file("minimize z: ")
    for k in range(1, CUSTOMERS + 1):
        if k == CUSTOMERS:
            util.write_content_to_file(f"t_{k};")
        else:
            util.write_content_to_file(f"t_{k} + ")
    util.write_new_line_to_file()
    util.write_new_line_to_file()

def generate_t_constraints():
    util.write_content_to_file_with_a_new_line("# t constraints")
    for k in range(1, CUSTOMERS + 1):
        for i in range(1, DELIVERY_BOYS + 1):
            for j in range(1, CUSTOMERS + 1):
                util.write_content_to_file(f"subject to t_{k}_{i}_{j}: ")
                util.write_content_to_file(f"t_{k} >= ")
                for p in range(1, j):
                    for m in range(1, CUSTOMERS + 1):
                        util.write_content_to_file(f"{WAIT_TIME_COEFFICIENTS[m-1]} * y_{i}_{p}_{m} + ")
                util.write_content_to_file_with_a_new_line(f"{WAIT_TIME_COEFFICIENTS[k-1]} * y_{i}_{j}_{k} - {M} * (1 - y_{i}_{j}_{k});")
    util.write_new_line_to_file()

def generate_turn_constraints():
    util.write_content_to_file_with_a_new_line("# turn constraints")
    for i in range(1, DELIVERY_BOYS + 1):
        for j in range(1, CUSTOMERS + 1):
            util.write_content_to_file(f"subject to turn_sum_{i}_{j}: ")
            for k in range(1, CUSTOMERS + 1):
                if k == CUSTOMERS:
                    util.write_content_to_file(f"y_{i}_{j}_{k} ")
                else:
                    util.write_content_to_file(f"y_{i}_{j}_{k} + ")
            util.write_content_to_file_with_a_new_line("<= 1;")
    util.write_new_line_to_file()

def generate_delivery_constraints():
    util.write_content_to_file_with_a_new_line("# delivery constraints")
    for k in range(1, CUSTOMERS + 1):
        util.write_content_to_file(f"subject to customer_delivery_{k}: ")
        for i in range(1, DELIVERY_BOYS + 1):
            for j in range(1, CUSTOMERS + 1):
                if i == DELIVERY_BOYS and j == CUSTOMERS:
                    util.write_content_to_file_with_a_new_line(f"y_{i}_{j}_{k} = 1;")
                else:
                    util.write_content_to_file(f"y_{i}_{j}_{k} + ")
    util.write_new_line_to_file()

def generate_y_constraints():
    util.write_content_to_file_with_a_new_line("# y constraints")
    for i in range(1, DELIVERY_BOYS + 1):
        for j in range(2, CUSTOMERS + 1):
            util.write_content_to_file(f"subject to y_dependency_{i}_{j}: ")
            for k in range(1, CUSTOMERS + 1):
                if k == CUSTOMERS:
                    util.write_content_to_file(f"y_{i}_{j}_{k} <= ")
                else:
                    util.write_content_to_file(f"y_{i}_{j}_{k} + ")
            for k in range(1, CUSTOMERS + 1):
                if k == CUSTOMERS:
                    util.write_content_to_file_with_a_new_line(f"y_{i}_{j-1}_{k};")
                else:
                    util.write_content_to_file(f"y_{i}_{j-1}_{k} + ")
    util.write_new_line_to_file()

util.set_file_name(FILENAME)
util.clear_file()

generate_t_variables()
generate_y_variables()

generate_objective_function()

generate_t_constraints()
generate_turn_constraints()
generate_delivery_constraints()
generate_y_constraints()