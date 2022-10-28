import sys
import os
sys.setrecursionlimit(2500)

filename = 'test-input'

with open(filename, 'r') as f:
    content = [x.strip() for x in f.readlines()]

ids = [int(x) for x in content]

with open('helper-vars.css', 'w') as f:
    necessary_vars = set(ids)
    for x in sorted(necessary_vars):
        print('div[data-integer-value="{0}"] {{ --my-integer-value: {0}; --my-string-value: "{0}" }}'.format(x), file=f)    
    print('', file=f)
    for x in sorted(necessary_vars):
        print('div[data-integer-value="{0}"] + div {{ --prior-div-integer-value: {0}; --prior-div-string-value: "{0}" }}'.format(x), file=f)

divs = '\n'

for input_id in ids:
    divs += '<div data-integer-value="{0}"></div>\n'.format(input_id)

with open('index-template.html', 'r') as f:
    content = f.read()

content = content.replace('[[DATA]]', divs)    

with open('index.html', 'w') as f:
    f.write(content)    
