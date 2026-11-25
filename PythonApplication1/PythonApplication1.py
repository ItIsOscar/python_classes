import re
with open("text.txt", "r") as file:
    body = file.read().lower()
    body = re.sub('[^a-z]', '', body)
    tmp_result = [(chr(i), len([j for j in body if j==chr(i)]) / len(body)) for i in range(0,256)]
tmp_result = [x for x in tmp_result if x[1]!=0]
print(tmp_result, sum([inner[1] for inner in tmp_result]))