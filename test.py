import math
from collections import Iterable
from functools import reduce
def add(x,y):
    return x+y
def fib(max):
    n = 0
    a = 0
    b = 1
    while n < max:
        print(b)
        c = a+b
        a = b
        b = c
        n += 1
def intersect(nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if not nums1 or not nums2:
            return []
        map = {}
        res = []
        
        for num in nums1:
            if num not in map:
                map[num]=1
            else:
                map[num]+=1
        print(map);
        for num in nums2:
            if num in map and map[num]>0:
                res.append(num)
                map[num]-=1
        return res
def f(x):
    return x*x
def fn(x,y):
    return x*10+y
def char2num(s):
     return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
def str2int(s):
    return reduce(fn, map(char2num,s))
def str2float(s):
    temp = s.split('.')
    #(map(char2num,temp[1]))
    first = int(reduce(fn,map(char2num,temp[0])))
    second = int(reduce(fn,map(char2num,temp[1])))
    t = 1.0
    for i in range(len(temp[1])):
        t*=0.1
    return first+second*t
    
def change(s):
    str = s[1:len(s)].lower()
    str1 = s[0].upper();
    return str1+str
def prod(L):
    def multiply(x,y):
        return x*y
    return reduce(multiply,L)
def by_score(t):
    return t[1]
def by_name(t):
    return t[0]
if __name__ == "__main__":
     s = '123.456'
     #print(str2float(s))
     N = [1,2,3,4,5,6,7]
     #L = [2,-1,5,88,-99]
     L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
     #L = ['adam', 'LISA', 'barT']
     str1=['bob', 'about', 'Zoo', 'Credit']
     print(sorted(str1,key=str.lower,reverse=True))
     #print(L[0][1])
     print(sorted(L,key=by_score))
     print(sorted(L,key= by_name))
     #print(list(map(change,L)))
     #print(prod(N))
