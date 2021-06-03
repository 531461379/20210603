#！/usr/bin/env python
# _*_ coding:utf-8 _*_
# @Time:2020/5/18 14:31

import random


def RandomStr(dataMat,number):
    slice=random.sample(dataMat,number)
    slice_str = "".join(slice)
    # print(slice_str)
    return slice_str

# if __name__ == "__main__":
str_five = RandomStr("asdsadasdasf",5)
int_eleven = RandomStr("15631469789496",11)
int_four = RandomStr("4561654",4)


