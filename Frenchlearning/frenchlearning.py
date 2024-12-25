import random
import json
def random_line_from_file(file_path):
    with open(file_path, "r") as file:
        lines = [json.loads(line) for line in file]
        return random.choice(lines)
w = random_line_from_file("C:/Users/furaribi/Documents/MySimpleProjects/Frenchlearning/fenchwords.txt")
print(w)