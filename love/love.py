import os
import time
import random
import string
import colorama
from random import randint
from colorama import Fore, Back, Style

colorama.init()

for i in range(1, 45):
    print(' ')

play = 0
while play == 0:
    left_spaces = randint(8, 80)

    loves = 8
    for i in range(1, 17):
        count = left_spaces
        while count > 0:
            print(' ', end=' ')
            count = loves
            while count > 0:
                if i == 1 and count == 4:
                    print('    ', end='')
                elif i < 3 and count == 5:
                    print('     ', end='')
                else:
                    print(Fore.RED + Style.BRIGHT + 'NGOC', end='')
                count -=1
            if i < 5:
                left_spaces = left_spaces -2
                loves +=1
            else:
                left_spaces = left_spaces +2
                loves -=1
                time.sleep(0.3)
                print('\n', end='')
        print('\n', end='')
        time.sleep(0.3)
        count = randint(8,80)
        while count > 0:
            print('', end='')
            count -=1
            print(Fore.MAGENTA + Style.BRIGHT + 'anh yeu em')
            time.sleep(0.3)
            print('\n', end='')
            time.sleep(0.3)