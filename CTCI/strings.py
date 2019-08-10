#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 12 18:04:17 2019

@author: mayankraj


cracking the coding interview String based questions
"""
"""
1.1 Implement an algorithm to determine if a string has all unique characters. What if u
cannot use an additional data structure
"""

# this is by using additional data structure
def unique_string(string1):
    hashset = set()
    for i in string1:
        if i in hashset:
            return False
        else:
            hashset.add(i)
        
    return True



#this is without any other data structure
def unique_string_withoutDS(string1):
    string1 =''.join(sorted(string1))
    for i in string1:
        if i == i+1:
            return False
    
    return True



"""
1.2 Given two strings, write a method to decide if one is permutation of the other

"""

def strings_permutation_of_each_other(str1, str2):
    if len(str1) != len(str2):
        return False
    str1 = ''.join(sorted(str1))
    str2 = ''.join(sorted(str2))
    if str1 == str2:
        return True
    return False
#another way to implement by counting the characters and appending in the count array
def strings_permutation_of_each_other2(str1, str2):
    if len(str1) != len(str2):
        return False
    list1 = [0]*256
    for i in str1:
        list1[ord(i)] += 1
        
    for i in str2:
        list1[ord(i)] -= 1
    for i in list1:
        if list1[i] < 0:
            return False
    
    return True


"""
1.3 URLify write a method to replace all spaces in a string with "%20". String has 
sufficient space at the end to hold the individual characters, and u are given 
true length of the string without the space
input - 'Mr John Smith    ', 13
output - 'Mr%20John%20Smith'
"""

def URLify(str1, length):
    arr = []
    for i in str1:
        if i.isspace():
            arr.append('%20')
        else:
            arr.append(i)
            
    str1 = ''.join(arr)
    return str1
        
   

"""
1.4 Palindrome Permutation
Given a string , write a function to check if it is permutation of a palindrome
"""  

def is_permutation_palindrome(str1):
    list1 = [0]*256
    count = 0
    for i in str1:
        list1[ord(i)] += 1
        
    if len(str1) % 2 == 0:
        for i in list1:
            if i%2 != 0:
                return False
    else:
        for i in list1:
            if i%2 != 0:
               count += 1
            if count > 1:
                return False
    
    return True
        
    
"""
1.5 One Away
There are three types of edits that can be performed on strings: insert a character, 
remove a character, or replace a character. given two strings write a method to check if
they are one away strings
"""    

def one_away_string(str1, str2):
    dict1 = set()
    
    count =0
    for i in str1:
        dict1.add(i)
    for i in str2:
        if i not in dict1:
            count += 1
    if count > 1:
        return False
    return True


"""
1.6 String Compression

Implement a method to perform basic string compression using the count of repeated 
characters. for example, aabcccccaaa becomes a2b1c5a3
If the compressed string is not smaller than the original string then return the 
original string

"""

def string_compression(str1):
    list1 = []
    count = 0
    for i in range (0,len(str1)):
        count += 1
        if (i + 1 >= len(str1) or str1[i] != str1[i+1]):
            list1.append(str1[i])
            list1.append(str(count))
            count = 0
    str2 =  ''.join(list1)
    if (len(str2) >= len(str1)):
        return str1
    else:
        return str2
        
        
    
def make_n_matrix():
    print("enter the number of rows")
    print()
    a = []
    n = int(input())
    #print("enter the number of colums")
    #m = int(input())
    print()
    print('enter each row for matrix, elemnts separated by space and rows by newline')
    for i in range(n):       
        row = input().split()
        for j in range(len(row)):
            row[j] = int(row[j])
            
        a.append(row)
    for row in a:
        for elem in row:
            print(elem, end=' ')
        print()
    
    return a
        
               

"""

1.8 Zero Matrix

Write an algorithm such that if an element in a M*N matrix is 0, its entire roq and 
columna re set to zero
"""

def make_zero_matrix(matrix):
    list_rows = [False]*len(matrix)
    list_col = [False]*len(matrix[0])
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if(matrix[i][j] == 0):
                list_rows[i] = True
                list_col[j] = True
    for i in range(len(list_rows)):
        if list_rows[i]:
            nullifyRow(matrix,i)
    for j in range(len(list_col)):
        if list_col[j]:
            nullifyCol(matrix,j)
    return matrix

def nullifyRow(matrix,row):
    for i in range(len(matrix[0])):
        matrix[row][i] = 0

def nullifyCol(matrix, col):
    for i in range(len(matrix)):
        matrix[i][col] = 0


def print_matrix(matrix):
    for row in matrix:
        for element in row:
            print(element,  end= ' ')
        print()

"""

1.9 string rotation
Assume you have a method isSubstring which checks if one word is substring of another.
Given two strings str1, str2, write code to check if str2 is a rotation of s1 using 
only one call to isSubstring.
Example - waterbottle and erbottlewat
"""


def string_rotation(str1, str2):
    str2 = str2 + str2
    if str1 in str2:
        return True
    else:
        return False
#answer = unique_string("abcdefghijklmnopqrstuvwxyza")
#answer = strings_permutation_of_each_other2("cdefagb","abcdefg")
#answer = URLify("Mr John Smith",13)
#answer = is_permutation_palindrome("intothetheitno")
#answer = one_away_string("mayank","maypol")
        
#matrix = [[0,2,3],[4,5,6],[7,8,9]]
#print(len(matrix[0]))
#print(range(len(matrix)))
#zero_matrix = make_zero_matrix(matrix)
#print_matrix(zero_matrix)
answer = string_rotation("mayankrajisgood","goodmayankrajis")
print(answer)
