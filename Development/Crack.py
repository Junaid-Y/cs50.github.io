from string import digits
from itertools import products

for passcode in product(digits, repeat = 4):
    print(*passcode)
    