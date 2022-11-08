import sys
import os
sys.setrecursionlimit(2500)

filename = 'input'

with open(filename, 'r') as f:
    content = [x.strip() for x in f.readlines()]

commands = [(x.split(' ')[0], int(x.split(' ')[1])) for x in content]

the_divs = {
    'forward': [],
    'up': [],
    'down': []
}
for command, distance in commands:
    the_divs[command].append(f'<div data-command="{command}" data-distance="{distance}"></div>')

with open('index-template.html', 'r') as f:
    content = f.read()

keys = the_divs.keys()
for key in keys:
    inner_divs = '\n'.join(the_divs[key])
    full_div = f'<div class="command-{key}">{inner_divs}</div>'
    the_divs[key] = full_div

dive_div = the_divs['forward'] + '\n' + the_divs['down']
surface_div = the_divs['forward'] + '\n' + the_divs['up']
updated_content = content.replace('[[DIVE-DATA]]', dive_div)
updated_content = updated_content.replace('[[SURFACE-DATA]]', surface_div)

with open('index.html', 'w') as f:
    f.write(updated_content)

generated_css = []

with open('helper-vars.css', 'w') as f:
    for idx in range(0, 100):
        print('div[data-distance="{idx}"] {{ --distance: {idx}px; --distance-as-string: "{idx}" }}'.format(idx=idx), file=f)
