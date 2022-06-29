import os
from pprint import pprint

result_dict = {}

for filename in os.listdir("task_3"):
    line_number = 0
    line_list = []
    with open(os.path.join("task_3", filename), 'r') as file:
        for line in file:
            line_number += 1
            line_list.append(line.rstrip('\n'))

        result_dict.update({line_number: {filename: line_list}})


pprint(sorted(result_dict.items()))
with open("result.txt", 'a') as file:
    for line_dict in result_dict:

            file.write(line)