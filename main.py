from notjson import NotJson

nj = NotJson()

input_file = ''

with open('test.njson', mode='r') as file:
    input_file = file.read()

python_dict = nj.dumps(input_file)

print(python_dict)