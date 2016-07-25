#!/usr/bin/env python
#yinmingwang
import math
def isSushu(x,y):
	for i in range(x,y):
		flag = 1;
		k = int(math.sqrt(x));
		for j in range(2,k):
			if i % j == 0:
				flag = 0;
				break;
		if flag == 1:
			print("%5d" %(i));

if __name__ == "__main__":
	x = int(raw_input("please input the first num: "));
	y = int(raw_input("please input the second num: "));
	isSushu(x,y);
