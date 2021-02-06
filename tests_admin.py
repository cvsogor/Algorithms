'''
Write a function that takes in a list of dictionaries with a key and list of integers and returns a dictionary with the standard deviation of each list.
Note that this should be done without using the numpy built in functions. Standard deviation can be calculated as sqrt(sum_i((x_i-mean)^2)/N)
Example:
input = [
    {
        'key': 'list1',
        'values': [4,5,2,3,4,5,2,3],
    },
    {
        'key': 'list2',
        'values': [1,1,34,12,40,3,9,7],
    }
]

output -> {'list1': 1.12, 'list2': 14.19}
'''
import numpy as np

def fun(data):
  new_dict = {}
  for i in data:
      new_dict[i['key']] = stdev(i['values'])
  return new_dict

def stdev(data):
  mu = np.mean(data)
  numerator = np.dot(data-mu, (data-mu).T)
  denominator = len(data)
  output = np.sqrt(numerator/denominator)
  return output



test_data = [
  {
      'key': 'list1',
      'values': [4,5,2,3,4,5,2,3],
  },
  {
      'key': 'list2',
      'values': [1,1,34,12,40,3,9,7],
  }
]
output = fun(test_data)
print(output)
-----------------------------------------------------
'''
Given a dictionary with weights, write a function that returns a key at random with a probability proportional to the weights.
 
weights = {'A': 1, 'B': 2}
random_key(weights) -> return A 33.3%, B 66.6%

weights = {'A': 1, 'B': 1}
random_key(weights) -> return A 50%, B 50%
'''

import numpy as np


def fun(data):
  val_sum = 0
  val_sum = np.sum([i for i in data.values()])
  val_prob = [i/val_sum for i in data.values()]
  key_list = [i for i in data.keys()]
  # new_dict = {}
  # for k, v in data.items():
  #   new_dict[k] = '{:.1%}'.format(v/val_sum)
  rand_key = np.random.choice(key_list, p=val_prob)
  return rand_key


test_data = {'A':1, 'B':2}
output = fun(test_data)
print(output)
------------------------------------------------------
'''
Given a JSON object with nested objects, write a function that flattens all the objects to a single key-value dictionary. Do not use the library that actually performs this function.
Example:
Input: {'a': {'b': 'c', 'd': 'e'}}
Output: {'a_b':'c', 'a_d':'e'}
'''

def fun(data):
  new_dict = {}
  prev_output = []
  for k, v in data.items():
    out = fun_helper(k, v, prev_output)
    for i in out:
      new_dict[i[0]] = i[1]
  return new_dict

def fun_helper(parent_key, child_dict, prev_output):
  for k,v in child_dict.items():
    if isinstance(v, dict):
      fun_helper(f'{parent_key}_{k}', v, prev_output)
    else:
      prev_output.append((f'{parent_key}_{k}', v))
  return prev_output

  
test_data = {'a': {'b':'c', 'd':{'e':'f'}}}
output = fun(test_data)
print(output)
---------------------------------------------------
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
  str1_list = list(str1)
  pos_store = 0
  for l in str1_list:
    if l in str2:
      pos = str2.find(l)
      if pos >= pos_store:
        pos_store = pos
      else:
        return False
    else:
      return False
  return True


string1 = 'abc'
string2 = 'asbsc'
string3 = 'acedb'
output1 = fun(string1, string2)
output2 = fun(string1, string3)
print(output1)
print(output2)
----------------------------------------------
'''
Given a list of integers, return a new list of integers so that the subsequent integers in the list get filtered out if they are less than the integer at a further index in the list.
 
Example 1:

n = [20,17,19,18,12,16,10,4,6,3]

output = [20,19,18,16,10,6,3]

Example 2:

n = [25,30,21,22,14,10,5,26]

output = [30,26]
'''

def fun(data):
  current_max = -1
  new_list = []
  for i in range(len(data)-1):
    if data[i] > max(data[i+1:]):
      new_list.append(data[i])
  new_list.append(data[-1])
  return new_list


test_data = [25, 30, 21, 22, 14, 10, 5, 26]
output = fun(test_data)
print(output)
-------------------------------------------------
'''
Given a list of integers, return a new list of integers so that the subsequent integers in the list get filtered out if they are less than the integer at a further index in the list.
 
Example 1:

n = [20,17,19,18,12,16,10,4,6,3]

output = [20,19,18,16,10,6,3]

Example 2:

n = [25,30,21,22,14,10,5,26]

output = [30,26]
'''

def fun(data):
  current_max = -1
  new_list = []
  for i in range(len(data)-1):
    if data[i] > max(data[i+1:]):
      new_list.append(data[i])
  new_list.append(data[-1])
  return new_list


test_data = [25, 30, 21, 22, 14, 10, 5, 26]
output = fun(test_data)
print(output)
