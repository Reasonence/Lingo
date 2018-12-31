import signal
import sys
from infer import infer

def handler(sig, frame):
        print('\n\nBye.')
        sys.exit(0)

signal.signal(signal.SIGINT, handler)

while True:
    name = input('Name: ')
    male, female, inference = infer(name)
    maximum = 90

    print('M ' + '▀'*int((male/maximum)*25))
    print('F ' + '▀'*int((female/maximum)*25))

    if inference == 'u':
        sex = 'UNISEX'
    elif inference == 'f':
        sex = 'FEMALE'
    else:
        sex = 'MALE'

    print('{} == {}'.format(name.upper(), sex))
    print('')