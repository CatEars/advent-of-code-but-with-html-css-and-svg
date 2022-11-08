import sys
import os
sys.setrecursionlimit(2500)

filename = 'input'
animation_delay = 0.1

with open(filename, 'r') as f:
    content = [x.strip() for x in f.readlines()]

commands = [(x.split(' ')[0], int(x.split(' ')[1])) for x in content]

base_animation_attributes = 'fill="freeze"'

animations = []
for idx, (command, distance) in enumerate(commands):
    begin_time = idx * animation_delay
    if command == 'up':
        animations.append(f'<animate attributeName="height" {base_animation_attributes} begin="{begin_time}s" by="-{distance}" dur="{animation_delay}" />')
    elif command == 'down':
        animations.append(f'<animate attributeName="height" {base_animation_attributes} begin="{begin_time}s" by="{distance}" dur="{animation_delay}" />')
    elif command == 'forward':
        animations.append(f'<animate attributeName="width" {base_animation_attributes} begin="{begin_time}s" by="{distance}" dur="{animation_delay}" />')

with open('index-template.html', 'r') as f:
    content = f.read()

animations_div = '\n' + '\n'.join(animations)
updated_content = content.replace('[[ANIMATION-DATA]]', animations_div)

with open('index.html', 'w') as f:
    f.write(updated_content)
