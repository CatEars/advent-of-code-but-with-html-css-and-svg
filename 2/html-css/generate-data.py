import sys
import os
sys.setrecursionlimit(2500)

filename = 'test-input'

with open(filename, 'r') as f:
    content = [x.strip() for x in f.readlines()]

commands = [(x.split(' ')[0], int(x.split(' ')[1])) for x in content]

the_divs = []
for command, distance in commands:
    the_divs.append(f'<div data-command="{command}" data-distance="{distance}"></div>')

div_string = '\n'.join(the_divs)

with open('index-template.html', 'r') as f:
    content = f.read()

updated_content = content.replace('[[DATA]]', div_string)    

with open('index.html', 'w') as f:
    f.write(updated_content)

generated_css = []

with open('helper-vars.css', 'w') as f:
    for idx in range(0, 100):
        print('div[data-distance="{idx}"] {{ --distance: {idx}; --distance-as-string: "{idx}" }}'.format(idx=idx), file=f)
