import sys
import os.path
import random

class ReadTable:
    """
    鍵を元にしてテーブルから文字を読み取る
    """

    table_list = []
    def read(self):
        file = open(os.path.abspath('./stored/table'))
        for line in file:
            self.table_list.append(line)

    def convert(self, key):
        if len(key) % 2 != 0:
            print("キーの形式が違います")
            sys.exit()
        key_list = list(key)
        cmbs = []
        for k in range(0, len(key_list), 2):
            p = int(key_list[k])
            n = int(key_list[k+1])
            cmbs.append((p, n))
        return cmbs

    def decypher(self, cmbs):
        word = ""
        for tpl in cmbs:
            for line in range(len(self.table_list)):
                for char in range(len(self.table_list[line])):
                    if tpl[0] == line and tpl[1] == char:
                        word += self.table_list[line][char]
        print(word)

    def getStrings(self):
        strings = ""
        for i in range(33, 127):
            strings += chr(i)
        return strings
    
    def createLine(self):
        clist = list(self.getStrings())
        random.shuffle(clist)
        return "".join(clist)



# reader = ReadTable()
# reader.read()
# 
# args = sys.argv
# cmbs = reader.convert(args[1]);
# reader.decypher(cmbs)


