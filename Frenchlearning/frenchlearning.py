import random
import json
def random_line_from_file(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
        chosen =random.choice(lines).strip()
        return json.loads(chosen)

words_path ="C:/Users/furaribi/Documents/MySimpleProjects/Frenchlearning/frenchwords.txt"
print(random_line_from_file(words_path))