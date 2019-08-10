#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 13:20:17 2019

@author: mayankraj
"""

class Node:
    def __init__(self,item):
        self.data = item
        self.next = None
        self.min_prev = 100000
        return


class Stack:
    def __init__(self):
        self.top = None
        self.minimum = 100000
    def push(self,item):
        if not isinstance(item,Node):
            item = Node(item)
        if self.top is None:
            self.top = item
        else:
            item.next = self.top
            self.top = item
        if item.data <= self.minimum:
            item.min_prev = self.minimum
            self.minimum  = item.data
        else:
            item.min_prev = None
        #item.next = self.top
        #self.top = item
        print("pushed to stack" + str(item.data))
    
    def pop(self):
        if self.is_empty():
            return None
        if self.top is not None:
            item = self.top
            self.top = self.top.next
            minm = self.minimum
            if item.data == minm:
                minm = item.min_prev
            self.minimum = minm
                
        
        return item.data
    
    def is_empty(self):
        return self.top is None
    
    def peek(self):
        return self.top.data
    """
    3.2 Implement a stack to find minimum element, 
    I imlemented this functionality in push and pop , see those methods to understand.
    Added two prop in the classes, one in node and one in Stack
    min_prev maintains the previous min for Node 
    minimum maintains the the minimum element of the stack
    """
    def min_elem(self):
        return self.minimum
        

    



"""
3.1

Implement n stacks using a single array
using two arrays here, to maintain top of each stack and next available index in the 
array

stackdata = [0,0,0,0,0,0,0.........]
topofstack = [-1,-1,-1,.......-1]
nextIndex = [1,2,3,4,5,6..........,-1] all indexes here pointing to the next index, but
the last one which means that the stackdata array is full
"""
class kstacks:
    def __init__(self, k,n):
        
        self.number_of_stacks = k
        self.size_of_array = n
        
        self.top_of_stacks = [-1]*k #-1 means that the stack is empty
        self.stack_data = [0]*n # 0 means that the element at the index is not set
        self.next_index = [ i + 1 for i in range(self.size_of_array) ]
        self.next_index[self.size_of_array - 1] = -1   
        
        self.next_available = 0
        
        return
        
    def is_empty(self,stack_number):
        return self.top_of_stacks[stack_number] == -1
    
    def is_full(self):
        return self.next_available == -1
    
    def push(self, stack_number, item):
        
        if self.is_full():
            return "Stack Overflow"
        
        insert_at = self.next_available
        
        self.next_available = self.next_index[self.next_available]
        
        self.stack_data[insert_at] = item
        
        self.next_index[insert_at] = self.top_of_stacks[stack_number]
        
        self.top_of_stacks[stack_number] = insert_at
        
    def pop(self,stack_number):
        if self.is_empty(stack_number):
            return None
        
        top = self.top_of_stacks[stack_number]
        
        self.top_of_stacks[stack_number] = self.next_index[self.top_of_stacks[stack_number]]
        
        self.next_index[top] = self.next_available
        self.next_available = top
        
        return self.stack_data[top]
        
        
"""s = kstacks(3,10)    
#s.top_of_stacks
#print(s.size_of_array) 
s.push(0,5)  
s.pop(0)"""


"""
3.3 
Stack of Plates: Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
composed of several stacks and should create a new stack once the previous one exceeds capacity. SetOfStacks. push() and SetOfStacks. pop() should behave identically to a single stack (that is, pop() should return the same values as it would if there were just a single stack).
FOLLOW UP
Implement a function popAt(int index) which performs a pop operation on a specific 
sub-stack

"""

class BigStack:
    def __init__(self):
        #self.size = size
        self.current_stack = 0
        self.all_stacks = []
        self.top = None
    
    def peek(self):
        x = self.all_stacks[self.current_stack]
        self.top = x.top
        return x.top
    
    
    class Stack:
        def __init__(self):
            self.top = None
            self.size = 0
        def push(self,item):
            if not isinstance(item,Node):
                item = Node(item)
            
            if self.is_full():
                return -1
            if self.top is None:
                self.top = item
                self.size += 1
            else:
                item.next = self.top
                self.top = item
                self.size += 1
            #item.next = self.top
            #self.top = item
            print("pushed to stack" + str(item.data))
        
        def pop(self):
            if self.is_empty():
                return None
            if self.top is not None:
                item = self.top
                self.top = self.top.next
            return item.data
        
        def is_empty(self):
            return self.top is None
        
        def is_full(self):
            return self.size >= 3
                
        
        def peek(self):
            return self.top.data
        
    
    
    def push(self,item):
        if self.all_stacks == []:
            x = self.Stack()
            x.push(item)
            self.all_stacks.append(x)
            #self.top = x.top
        else:
            x = self.all_stacks[self.current_stack]
            z = x.push(item)
            if z == -1:
                y = self.Stack()
                y.push(item)
                self.all_stacks.append(y)
                self.current_stack += 1
                #self.top = y.top
            """else:
                x.push(item)"""
                #self.top = x.top
                
    def pop(self):
        if self.all_stacks == []:
            return None
        else:
            x = self.all_stacks[self.current_stack]
            temp = x.pop()
            if x.is_empty():
                self.current_stack -= 1
                self.all_stacks.pop()
            return temp
    #method to pop from a specific substack
    def pop_at_index(self,stack_number):
        x = self.all_stacks[stack_number]
        
        return x.pop()
                
               

"""
3.4
Queue via stacks: Implement a MyQueue class which implements a queue using two stacks

"""

class MyQueue:
    def __init__(self):
        self.stack1 = Stack()
        self.size = 0
        self.stack2 = Stack()
        return
        
    def queue(self,item):
        if not isinstance(item,Node):
                item = Node(item)
        if self.stack1.top is None:
            self.stack1.top = item
            self.size += 1
        else:
            item.next = self.stack1.top
            self.stack1.top = item
            self.size += 1
    
    def is_empty(self):
            return self.stack1.top is None
        
    def deque(self):
        if self.is_empty():
            return None
        i = 0
        while i < self.size:
            x = self.stack1.pop()
            self.stack2.push(x)
            i += 1
        temp = self.stack2.pop()
        self.size -= 1
        j = 0
        while j < self.size:
            x = self.stack2.pop()
            self.stack1.push(x)
            j += 1
        return temp
                



node1 = Node(18889)
node2 = Node(2000)
node3 = Node(458)
node4 = Node(1786)

que = MyQueue()
for item in [node1, node2, node3, node4]:
    que.queue(item)
    

b = BigStack()
for item in [node1, node2, node3]:
    b.push(item)
b.push(node4)
    

print(node1.next)
s = Stack()
for item in [node1, node3, node2,node4]:
    
    s.push(item)
    print(s.top.data)
    print(item.min_prev)
    print(s.min_elem())
print(s.get_stack())
print(s.peek())
print(s.top.data)


