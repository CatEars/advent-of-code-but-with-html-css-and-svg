loops = 1000

with open('template/nth-child-loop.css', 'w') as f:
    for i in range(loops):
        print(':nth-child({0}) {{ --nth-child: {0} }}'.format(i), file=f)    
    print('', file=f)
    for i in range(loops):
        print('[data-integer-value = "{0}"] {{ --integer-value: {0} }}'.format(i), file=f)    


