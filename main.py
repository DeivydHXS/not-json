from notjson import NotJson

nj = NotJson()

json = '{ key: 4 key2: false key3: \'str\' }'

for e in nj.scan(json):
    print(e.type, e.lexeme)