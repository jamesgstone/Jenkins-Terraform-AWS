import json

f = '{ "name":"John_r", "age":"30", "city":"New York_re"}'

y = json.loads(f)

y["age"] = 50

# print(y)
# converted = y.sub(r'-_r\b', '_x', y.sub(r'-_er\b', '_x', f))
# print(y)


for i,j in y.items():
    if j