import gmpl_utility as util
import random

FILENAME = "diet.txt"

NUMBER_OF_PRODUCTS = 17500
COSTS_PER_SERVING = []
NUTRIENT_INFORMATION = []
STOCK_PER_PRODUCT = 10

NUMBER_OF_NUTRIENTS = 20
NUTRIENT_BOUNDS = [
    (1600, 2400),
    (50, 175),
    (44, 78),
    (225, 325),
    (25, 38),
    (0, 50),
    (700, 900),
    (75, 90),
    (2600, 3400),
    (8, 18),
    (1000, 1300),
    (15, 20),
    (15, 20),
    (90, 120),
    (1.1, 1.2),
    (1.1, 1.3),
    (14, 16),
    (1.3, 1.7),
    (400, 600),
    (2.4, 2.8),
]

for _ in range(NUMBER_OF_PRODUCTS):
    COSTS_PER_SERVING.append(round(random.uniform(0, 2), 2))

for _ in range(NUMBER_OF_PRODUCTS):
    temp = []
    for i in range(NUMBER_OF_NUTRIENTS):
        temp.append(round(random.uniform(NUTRIENT_BOUNDS[i][0] * 0.05, NUTRIENT_BOUNDS[i][1] * 0.2), 2))
    NUTRIENT_INFORMATION.append(temp)

print("Preprocessing done!")

def generate_x_variables():
    util.write_content_to_file_with_a_new_line("# x variables")
    for i in range(1, NUMBER_OF_PRODUCTS + 1):
        util.write_content_to_file_with_a_new_line(f"var x_{i} >= 0, <= {STOCK_PER_PRODUCT};")
    util.write_new_line_to_file()

def generate_objective_function():
    util.write_content_to_file_with_a_new_line("# objective function")
    util.write_content_to_file("minimize z: ")
    for i in range(1, NUMBER_OF_PRODUCTS + 1):
        if i != NUMBER_OF_PRODUCTS:
            util.write_content_to_file(f"{COSTS_PER_SERVING[i - 1]} * x_{i} + ")
        else:
            util.write_content_to_file_with_a_new_line(f"{COSTS_PER_SERVING[i - 1]} * x_{i};")
    util.write_new_line_to_file()

def generate_dietary_constraints():
    util.write_content_to_file_with_a_new_line("# dietary constraints")
    for i in range(NUMBER_OF_NUTRIENTS):
        util.write_content_to_file(f"subject to nutrient_{i + 1}: ")
        util.write_content_to_file(f"{NUTRIENT_BOUNDS[i][0]} <= ")
        for j in range(NUMBER_OF_PRODUCTS):
            if j != NUMBER_OF_PRODUCTS - 1:
                util.write_content_to_file(f"{NUTRIENT_INFORMATION[j][i]} * x_{j + 1} + ")
            else:
                util.write_content_to_file(f"{NUTRIENT_INFORMATION[j][i]} * x_{j + 1} ")
        util.write_content_to_file_with_a_new_line(f"<= {NUTRIENT_BOUNDS[i][1]};")
    util.write_new_line_to_file()

util.set_file_name(FILENAME)
util.clear_file()

generate_x_variables()
print("x variables generated!")

generate_objective_function()
print("Objective function generated!")

generate_dietary_constraints()
print("Dietary constraints generated!")

print("Done!")