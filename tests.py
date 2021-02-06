'''
Given a dictionary with weights, write a function that returns a key at random with a probability proportional to the weights. Also return the associated probability in "0.00%" format. Both outputs should form a tuple.
 
weights = {'A': 1, 'B': 2}
random_key(weights) -> ('A', '33.3%') or ('B', '66.67%')

'''
import random

def fun(data):
    probFormat = {}
    s = sum(data.values())
    for k in data:
        g = float("{:.2f}".format(data[k] / s))
        probFormat[k] = str(g) + '%'
        #print(probFormat[k])
    choice = random.choices(list(data.keys()), weights=data.values(), k=1)
    return choice, probFormat[choice[0]]


test_data = {'A':1, 'B':2}
output = fun(test_data)
print(output)
-------------------------------------------------------------------
'''
Given a JSON object with nested objects, write a function that flattens all the objects to a single key-value dictionary. Do not use the library that actually performs this function.

Examples:

Input: {'a': {'b': 'c', 'd': 'e'}}
Output: {'a_b':'c', 'a_d':'e'}

Input: {'a': {'b': 'c', 'd': {'e': 'f'}}}
Output: {'a_b':'c', 'a_d_e':'f'}
'''

def recfun(prefix, data, dic):
    for k in data:
        newkey = prefix
        if newkey != '':
            newkey = newkey + '_' + k
        else:
            newkey = k

        if isinstance(data[k],dict):
            recfun(newkey, data[k], dic)
        else:
            dic[newkey] = data[k]
      
    return dic

def fun(data):
    dic = {}
    recfun('', data, dic)
    return dic

test_data1 = {'a': {'b':'c', 'd':'e'}}
output1 = fun(test_data1)
print(output1)
print('--------------------')
test_data2 = {'a': {'b':'c', 'd':{'e':'f'}}}
output2 = fun(test_data2)
print(output2)

-----------------------------------------------
'''
Given two strings, string1 and string2, find out if string1 is a subsequence of string2.
A subsequence is a sequence that can be derived from another sequence by deleting some elements without changing the order of the remaining elements.

Example:
string1 = 'abc'
string2 = 'asbsc'
string3 = 'acedb'

isSubSequence(string1, string2) -> True
isSubSequence(string1, string3) -> False
'''

def fun(str1, str2):
    w = 0
    for c in str1:
        if c == str2[w]:
            w += 1
        else:
            while c != str2[w]:
                w += 1
                if w >= len(str2):
                    return False
        
    return True


string1 = 'abc'
string2 = 'asbsc'
string3 = 'acedb'
output1 = fun(string1, string2)
print(output1)
output2 = fun(string1, string3)
print(output2)
-----------------------------------------------
'''
Given an array of integers N, return another array of integers M such that the subsequent integers in array N get filtered out if they are less than the integers at the subsequent indices in the array N.
 
Example 1:

input = [20,17,19,18,12,16,10,4,6,3]

output = [20,19,18,16,10,6,3]

Example 2:

input = [25,30,21,22,14,10,5,26]

output = [30,26]
'''

def fun(data):
    output = []
    l = len(data) - 1
    
    current = data[l]
    output.append(current)
    l -= 1
    
    while l >=0:
        if data[l] > current:
            current = data[l]
            output.append(current)
        l -= 1
        
    return list(reversed(output))


#test_data = [25, 30, 21, 22, 14, 10, 5, 26]
test_data = [20,17,19,18,12,16,10,4,6,3]
output = fun(test_data)
print(output)
-----------------------------------------------
