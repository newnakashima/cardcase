import sys
import getch

from randomPass import PassGenerator

def password():
    argv = sys.argv
    minimum_letter = argv[1] if len(argv) > 1 else "12"
    maximum_letter = argv[2] if len(argv) > 2 else "16"
    sign_letter    = argv[3] if len(argv) > 3 else "1"
    number_letter  = argv[4] if len(argv) > 4 else "1"
    capital_letter = argv[5] if len(argv) > 5 else "1"
    
    conditions = [minimum_letter, maximum_letter, sign_letter, number_letter, capital_letter]
    mapped = map(lambda x: int(x), conditions)
    cond = list(mapped)
    
    gen = PassGenerator()
    print(gen.genpass(*cond))
    print("Press g to generate new one. Any other key to exit")
    try:
        i = getch.getch()
        if i == 'g':
            password()
        else:
            sys.exit()
    except KeyboardInterrupt:
        print("終了します")
try:
    password()
    
except KeyboardInterrupt:
    print("終了します")
