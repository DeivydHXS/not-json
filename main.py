from notjson import NotJson

nj = NotJson()

input_file = ''

with open('test.njson', mode='r') as file:
    input_file = file.read()

toks = nj.scan(input_file)

for e in toks:
    print(e.type, e.lexeme)