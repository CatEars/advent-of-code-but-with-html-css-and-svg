import sys
import os
sys.setrecursionlimit(2500)

filename = 'test-input'

with open(filename, 'r') as f:
    content = [x.strip() for x in f.readlines()]

commands = [(x.split(' ')[0], int(x.split(' ')[1])) for x in content]
forwards = [x for x in commands if x[0] == 'forward']

with open('helper-vars.css', 'w') as f:
    necessary_vars = set([id for (cmd, id) in forwards])
    for x in sorted(necessary_vars):
        print('div[data-integer-value="{0}"] {{ --my-integer-value: {0}; --my-string-value: "{0}" }}'.format(x), file=f)    

divs = '\n'

for (cmd, id) in forwards:
    divs += '<div data-integer-value="{0}"></div>\n'.format(id)

with open('index-template.html', 'r') as f:
    content = f.read()

content = content.replace('[[FORWARDS-DATA]]', divs)    

with open('index.html', 'w') as f:
    f.write(content)    
