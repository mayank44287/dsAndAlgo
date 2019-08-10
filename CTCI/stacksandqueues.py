#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 16:08:24 2019
this file uses in build python lists to create stack and queue. This is not recommended
as this increses the time comlexity but for the time being it can be used. See the other
stack and queue file for another way of implementation
@author: mayankraj
"""

class Queue:
    def __init__(self):
        self.items = []
    
    def add(self,item):
        self.items.append(item)
        
    def remove(self):
        self.items.pop(0)
    
    def is_empty(self):
        return self.items == []
    
    def peek(self):
        if not self.is_empty():
            return self.items[0]
        
    def get_queue(self):
        return self.items
    

class Stack:
    def __init__(self):
        self.items = []
    
    def push(self,item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
    
    def get_stack(self):
        return self.items
    
    def is_empty(self):
        return self.items == []
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]










q = Queue()
q.add(1)
q.add(2)
q.add(3)   
print(q.get_queue())

print(q.peek())
q.remove()

s = Stack()
s.push(5)
s.push(6)
s.push(7)
print(s.get_stack())
s.pop()
print(s.get_stack())
s.is_empty()
s.peek()