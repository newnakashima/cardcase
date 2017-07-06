import sys
import random

class PassGenerator:
    """
    ランダムなパスワードを生成するクラス
    """
    def int_rand(self, start, end, step):
        random.seed()
        value = random.randrange(start, end+1, step)
        return value
    
    def sign_rand(self):
        value = self.int_rand(33, 60, 1)
        if (value > 47 and value <= 54):
            value += 10
        elif (value > 54):
            value += 36
        return value
    
    def genpass(self, minl = 8, maxl = 16, sig = 1, num = 1, cap = 1):
        """
        minl: 最小文字数
        maxl: 最大文字数
        sig:  記号文字数
        num:  数字文字数
        cap:  大文字文字数
        """
        if minl == maxl:
            length = minl
        else:
            length = self.int_rand(minl, maxl, 1)
    
        s_letters = []
        for c in range(sig):
            code = self.sign_rand()
            s_letters.append(code)
        n_letters = []
        for c in range(num):
            code = self.int_rand(48, 57, 1)
            n_letters.append(code)
        c_letters = []
        for c in range(cap):
            code = self.int_rand(65, 90, 1)
            c_letters.append(code)
    
        i_letters_list = [s_letters, n_letters, c_letters]
    
        letters = []
        for c in range(length - (sig + num + cap)):
            code = self.int_rand(97, 122, 1)
            letters.append(code)
        
        for i in i_letters_list: letters.extend(i)
    
        string = []
        for l in letters:
            string.append(chr(l))
    
        random.shuffle(string)
        result = "".join(string)
        print(result)
