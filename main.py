from notjson import NotJson

nj = NotJson()

input_file = ''

with open('test.njson', mode='r') as file:
    input_file = file.read()

python_dict = nj.loads(input_file)
print('Python dictionary')
print(python_dict)

print()
print('Not json string')
not_json_string = nj.dumps(python_dict)
print(not_json_string)
