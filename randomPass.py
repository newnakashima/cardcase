import sys
import random

def int_rand(start, end, step):
    random.seed()
    value = random.randrange(start, end, step)
    return value

def loop_input(message):
    str = ""
    while True:
        str = input(message)
        if not str.isdigit():
            print("数字を入力してください")
            return loop_input(message)
        else:
            return str

try:
    argv = sys.argv
    minimum_letter = argv[1] if len(argv) > 1 else ""
    maximum_letter = argv[2] if len(argv) > 2 else ""
    sign_letter    = argv[3] if len(argv) > 3 else ""
    number_letter  = argv[4] if len(argv) > 4 else ""
    capital_letter = argv[5] if len(argv) > 5 else ""

    if minimum_letter == "":
        minimum_letter = loop_input("最小文字数: ")
    if maximum_letter == "":
        maximum_letter = loop_input("最大文字数: ")
    if sign_letter == "":
        sign_letter = loop_input("最小記号文字数: ")
    if number_letter == "":
        number_letter = loop_input("最小数字文字数: ")
    if capital_letter == "":
        capital_letter = loop_input("最小大文字文字数: ")

    ok = ""
    while True:
        print("\n\n")
        print(f"最小文字数:       {minimum_letter}")
        print(f"最大文字数:       {maximum_letter}")
        print(f"最小記号文字数:   {sign_letter}")
        print(f"最小数字文字数:   {number_letter}")
        print(f"最小大文字文字数: {capital_letter}")
        print("\n\n")
        print("以上でよろしいですか?: y/n")
        ok = input()
        if ok != 'y' and ok != 'n':
            print("yもしくはnを入力してください")
        else:
            break
        
    if ok == 'y':
        length = int_rand(minimum_letter, maximum_letter, 1)
        print("y")
    else:
        print("n")

except KeyboardInterrupt:
    print("終了しました")
