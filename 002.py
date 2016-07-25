#!/usr/bin/env python
#yinmingwang
profit = int(raw_input("please input profit: "));
bouns = 0;
profitinterval = [0, 100000, 200000, 400000, 600000, 1000000];
rates = [0.1, 0.075, 0.05, 0.03, 0.015, 0.01];
for i in range(0,6):
	if profit > profitinterval[5-i]:
		bouns += (profit - profitinterval[5-i])*rates[5-i];
		profit = profitinterval[5-i];
print(bouns);
