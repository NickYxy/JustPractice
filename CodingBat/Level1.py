__author__ = 'nickyuan'

#missing_char
'''Given a non-empty string and an int n, 
return a new string where the char at index n has been removed. 
The value of n will be a valid index of a char in the original string 
(i.e. n will be in the range 0..len(str)-1 inclusive).

missing_char('kitten', 1) → 'ktten'
missing_char('kitten', 0) → 'itten'
missing_char('kitten', 4) → 'kittn'
'''
def missing_char(str, n):
  front = str[:n]
  back = str[n+1:]
  return front + back


#front_back
'''
Given a string, return a new string where the first and last chars have been exchanged.


front_back('code') → 'eodc'
front_back('a') → 'a'
front_back('ab') → 'ba'
'''
def front_back(str):
    if len(str) <= 1:
        return str
    mid = str[1:len(str) - 1]
    # mid = str[1:-1]

    return str[len(str) - 1] + mid + str[0]


#front3
'''

Given a string, we'll say that the front is the first 3 chars of the string. 
If the string length is less than 3, the front is whatever is there. 
Return a new string which is 3 copies of the front.


front3('Java') → 'JavJavJav'
front3('Chocolate') → 'ChoChoCho'
front3('abc') → 'abcabcabc'
'''
def front3(str):
  if len(str) <= 3:
    return str * 3
  else:
    return str[:3] * 3


#string_splosion
'''
Given a non-empty string like "Code" return a string like "CCoCodCode".


string_splosion('Code') → 'CCoCodCode'
string_splosion('abc') → 'aababc'
string_splosion('ab') → 'aab'
'''
def string_splosion(str):
  str1 = ''
  for i in range(len(str)):
    str1 = str1 + str[:i+1]
  return str1

#array_count9
'''

Given an array of ints, return the number of 9's in the array.


array_count9([1, 2, 9]) → 1
array_count9([1, 9, 9]) → 2
array_count9([1, 9, 9, 3, 9]) → 3
'''
def array_count9(nums):
  count = 0
  # Standard loop to look at each value
  for num in nums:
    if num == 9:
      count = count + 1

  return count