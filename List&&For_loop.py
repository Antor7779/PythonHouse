Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#list
numbers=[0,1,2,3,4,5,6,7,8,9]
len(numbers)
10
numbers[1]
1
numbers[2]
2
>>> numbers[5]
5
>>> numbers[9]
9
>>> #numbers=[len(numbers)-1]
>>> for number in numbers:
...     print(number)
... 
...     
0
1
2
3
4
5
6
7
8
9
>>> for number in numbers:
...     print(number**2)
... 
...     
0
1
4
9
16
25
36
49
64
81
>>> for number in numbers:
...     print(number**5)
... 
...     
0
1
32
243
1024
3125
7776
16807
32768
59049
>>> for number in numbers:
...     print(number**9)
... 
...     
0
1
512
19683
262144
1953125
10077696
40353607
134217728
387420489
