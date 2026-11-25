import re
#files_list = ("Доастфаты", "Толстой Лев. Повести и рассказы - royallib.com")
author_list = ("Jack London", "Emily Bronte")
file_list = (("first_literature.txt", 0), ("second_literature.txt", 1), ("third_literature.txt", 2))
matrix_symbols = [[[0 for x in range(97, 123)] for i in range(97, 123)] for j in file_list]
for literature in file_list:
    lenght = 0
    with open("./" + literature[0], "r") as file:
        for line in file:   
            line = line.lower()
            line = re.sub(f"[^a-z]", '', line)
            lenght = lenght + len(line)
            tmp = [x for x in zip(line[:-1], line[1:])]
            for x in tmp:
                matrix_symbols[literature[1]][ord(x[0]) - 97][ord(x[1]) - 97] += 1
        matrix_symbols[literature[1]] = [[matrix_symbols[literature[1]][i - 97][j - 97] / lenght for i in range(97, 123)] for j in range(97, 123)]
        #print(matrix_symbols[literature[1]])

ind_closses_match = 3
first_sum_diff =  sum([sum([abs(matrix_symbols[0][j - 97][i - 97] - matrix_symbols[2][j - 97][i - 97]) for i in range(97, 123)]) for j in range(97, 123)])
second_sum_diff = sum([sum([abs(matrix_symbols[1][j - 97][i - 97] - matrix_symbols[2][j - 97][i - 97]) for i in range(97, 123)]) for j in range(97, 123)])
if first_sum_diff > second_sum_diff:
    print(author_list[0])
else:
    print(author_list[1])








# tmp = (x for x in zip(line[:]. line[1:]))
#             for x in tmp:
#                 matrix_symbols[literature[1]][x[0]][x[1]] += 1
    
# with open("text.txt", "r") as file:
#     body = file.read().lower()
#     body = re.sub('[^a-z]', '', body)
#     tmp_result = [(chr(i), len([j for j in body if j==chr(i)]) / len(body)) for i in range(0,256)]
# tmp_result = [x for x in tmp_result if x[1]!=0]
# print(tmp_result, sum([inner[1] for inner in tmp_result]))