
import math

class NumberTrans:

    # common
    NUM_2: int = 2
    NUM_8: int = 8
    NUM_10: int = 10
    NUM_16: int = 16
    NUM_62: int = 62

    def __new__(cls, *args):
        print('new')
        #return super().__new__(cls)
        return object.__new__(cls)

    def __init__(self, name, pw):
        print('init')
        #super().__init__()

    def validator_str(str_num16: str) -> bool:
        CODEC = '0123456789abcdef'
        for str_item in str_num16:
            if not str_item in CODEC:
                return False
        return True

    def trans_10to2_v1(src_num:int):
        rtn_num = []
        while src_num>0:
            rtn_num.insert(0,str(src_num%2))
            src_num>>=1
        return ''.join(rtn_num)

    def trans_10to8_v1(src_num:int):
        rtn_num = []
        while src_num>0:
            rtn_num.insert(0,str(src_num%8))
            src_num>>=3
        return ''.join(rtn_num)

    def trans_10to16_v1(src_num:int):
        code = '0123456789ABCDEF'
        rtn_num = []
        while src_num>0:
            rtn_num.insert(0,str(code[src_num%16]))
            src_num>>=4
        return ''.join(rtn_num)

    # Num 2~9
    def trans_10to_num_v2(src_num:int, dest_num:int):
        rtn_num = []
        while src_num>0:
            src_num, remain = divmod(src_num,dest_num)
            rtn_num.insert(0, str(remain))
        return ''.join(rtn_num)

    def trans_10to16_v2(src_num: int) -> str:
        code: str = '0123456789ABCDEF'
        rtn_num: list = []
        while src_num>0:
            src_num, remain = divmod(src_num,16)
            rtn_num.insert(0,str(code[remain]))
        return ''.join(rtn_num)

    def trans_10to_num_v3(src_num: int, dest_num: int) -> str:
        src_num, remain = divmod(src_num, dest_num)
        if src_num == 0:
            return str(remain)
        else:
            return NumberTrans.trans_10to16_v3(src_num) + str(remain)

    def trans_10to16_v3(src_num: int) -> str:
        code: str = '0123456789ABCDEF'
        src_num, remain = divmod(src_num,16)
        if src_num == 0:
            return code[remain]
        else:
            return NumberTrans.trans_10to16_v3(src_num) + code[remain]

    def trans_10to62(src_num:int) -> str:
        code: str = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        rtn_num: list = []
        while src_num>0:
            src_num, remain = divmod(src_num,62)
            rtn_num.insert(0,str(code[remain]))
        return ''.join(rtn_num)

    ########
    def trans_num_to10(src_num: str, desc_num: int) -> int:
        rtn_num: int = 0
        src_num: str = reversed(str(src_num))
        for idx, digit in enumerate(src_num):
            rtn_num += int(digit) * pow(desc_num, idx)
        return rtn_num

    def trans_16to10(src_num: str) -> int:
        src_num = src_num.lower()
        CODEC = '0123456789abcdef'
        rtn_num: int = 0
        src_num: str = reversed(str(src_num))
        for idx, digit in enumerate(src_num):
            rtn_num += CODEC.find(digit) * pow(len(CODEC), idx)
        return rtn_num

    def trans_62to10(src_num: str) -> int:
        CODEC = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        rtn_num: int = 0
        src_num: str = reversed(str(src_num))
        for idx, digit in enumerate(src_num):
            rtn_num += CODEC.find(digit) * pow(len(CODEC), idx)
        return rtn_num

    def trans_62to10_v2(src_num: str) -> int:
        CODEC = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        rtn_num: int = 0 
        idx: int = 0
        for str_item in reversed(src_num):
            rtn_num += CODEC.find(str_item) * pow(len(CODEC), idx)
            idx += 1
        return rtn_num

    def trans_62to10_v3(src_num: str) -> int:
        CODEC = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        rtn_num: int = 0
        for idx, digit in enumerate(reversed(src_num)):
            rtn_num += CODEC.find(digit) * pow(len(CODEC), idx)
        return rtn_num

    #######
    def trans_2to8(src_num: str):
        rtn_num: list = []
        int_item: int = 0
        src_num: str = reversed(str(src_num))

        for i in range(1,len(src_num)/3):
            for idx, digit in enumerate(src_num):
                int_item += int(digit) * pow(2, idx)
            rtn_num.insert(0, int_item)

        return ''.join(rtn_num)
        
    def test_func(src_num: str):
        # init
        max_num = 0
        sum_num = 0
        result_num = []
        cnt_num = 0

        for i in reversed(src_num):
            cnt_num += 1
            sum_num += int(i) * pow(2, max_num)

            # foot
            max_num += 1
            if max_num > 2:
                max_num = 0
                result_num.insert(0, str(sum_num))
                sum_num = 0
            
            if cnt_num == len(src_num):
                result_num.insert(0, str(sum_num))
            
        return ''.join(result_num)

    def trans_2to16(src_num: str):
        return ''
    def trans_2to62(src_num: str):
        return ''

    def trans_8to2(src_num: str):
        return ''
    def trans_8to16(src_num: str):
        return ''
    def trans_8to62(src_num: str):
        return ''
    
    def trans_16to2(src_num: str):
        return ''
    def trans_16to8(src_num: str):
        return ''
    def trans_16to62(src_num: str):
        return ''

    def trans_62to2(src_num: str):
        return ''
    def trans_62to8(src_num: str):
        return ''
    def trans_62to16(src_num: str):
        return ''

