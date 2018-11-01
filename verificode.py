# _*_ coding:utf-8 _*_
# Author: daihaijun
# For python3.x

"""
生成6位随机验证码
写一个6位随机验证码程序（使用random模块),要求验证码中至少包含一个数字、一个小写字母、一个大写字母.
"""

import string
import random

str_random = []
str1 = random.sample(string.ascii_lowercase,1)
str2 = random.sample(string.ascii_uppercase,1)
str3 = random.sample(string.digits,1)
str4 = random.sample(string.ascii_letters + string.digits,3)

str_random = str1+str2+str3+str4
random.shuffle(str_random)
print(str_random)
