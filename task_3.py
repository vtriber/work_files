import os

def merging_files(folder_name):
    result_dict = {}

    for filename in os.listdir(folder_name):
        line_number = 0
        line_list = []
        with open(os.path.join(folder_name, filename), 'r') as file:
            for line in file:
                line_number += 1
                line_list.append(line.rstrip('\n'))

            result_dict.update({line_number: [filename, line_list]})

    with open("result.txt", 'a') as file:
        for key, line_list in sorted(result_dict.items()):
            file.write(line_list[0] + '\n')
            file.write(str(key) + '\n')
            for line in line_list[1]:
                file.write(line + '\n')

merging_files('task_3')