#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 24 20:44:28 2019

@author: mayankraj
"""

class ListNode:

    def __init__(self,data = None):
        self.data = data
        self.next = None
        self.left = None
        return
        
    def has_value(self,value):
        if self.data == value:
            return True
        else:
            return False


class SingleLinkedList:
    
    current = None    
    def __init__(self):
        
        self.head = None
        self.tail = None
        #self.current = None
        return
    
    def add_list_item(self,item):
        if not isinstance(item, ListNode):
            item = ListNode(item)
        
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
            
        self.tail = item
        
    def list_length(self):
        count = 0
        current_node = self.head
        while current_node is not None:
            count += 1
            current_node = current_node.next
        return count
    
    def output_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next
    
    def delete_node(self, item):
        currentNode = self.head
        
        #check if head is the node to be removed
        if currentNode is not None:
            if currentNode.data == item:
                self.head = currentNode.next
                currentNode = None
                return
        #check for other nodes
        
        while currentNode is not None:
            if currentNode.data == item:
                break
            prev = currentNode
            currentNode = currentNode.next
        
        #if node is not present in the list
        if currentNode == None:
            return
        #unlink the prev node
        prev.next = currentNode.next
        currentNode = None
    #2.1    
    def remove_duplicates(self):
        currentNode = self.head
        hashset = []
        while currentNode is not None:
            if currentNode.data not in hashset:
                hashset.append(currentNode.data)     
            currentNode = currentNode.next
        x = SingleLinkedList()
        
        for i in hashset:
            print(i)
            x.add_list_item(i)
        return x
    #2.1
    def remove_duplicates_without_buffer(self):
        currentNode = self.head
        prev = currentNode
        while currentNode is not None:
            temp = currentNode.next
            
            while temp is not None:
                if temp.data == currentNode.data:
                    prev.next = temp.next
                prev = temp    
                temp = temp.next
            currentNode = currentNode.next
        return self
    
    #2.2 return kth to last element
    def return_kth_to_last(self,k):
        currentNode = self.head
        
        i = 0
        
        length = self.list_length() - k
        while i < length:
            prev = currentNode.data
            currentNode = currentNode.next
            i += 1
        return prev
    #2.3 Delete Middle Node, i.e any node but the first or last node
    def delete_middle_node(self,item):
        if self.head.data == item or self.tail.data == item:
            return
        else:
            self.delete_node(item)
            
    
    #2.4 Partition: Partition a list around a value x, such that all nodes less than
    # x come before all nodes greater than or equal to x. If x is contained within the 
    #list then it has to appear in the right partition
    
    def partition_list(self,x):
        list1 = []
        list2 = []
        currentNode = self.head
        
        while currentNode is not None:
            if currentNode.data >= x:
                list2.append(currentNode.data)
            else:
                list1.append(currentNode.data)
            currentNode = currentNode.next
        
        listnew = SingleLinkedList()
        print("list1")
        for i in list1:
            print(i)
            
        print("list2")
        for i in list2:
            print(i)
        print("///////")
        for i in list1:
            listnew.add_list_item(i)
        
        for i in list2:
            listnew.add_list_item(i)
            
        return listnew
            
     #2.5 Sum Lists
    """
    You have two numbers represented by a linked list, where each node contains a single
    digit. The digits are stored in reverse order, such that 1's digit is at the head
    of the list.Write a function that adds the two numbers and returns the sum as linked
    list
    i/p = 7->1>6 + 5->9->2 i.e 617 + 295
    o/p = 2->1->9 i.e 912

    """  
    def sum_lists(self,list1, list2):
        list1head = list1.head
        list2head = list2.head
        carry = 0
        summation = []
        
        len1 = list1.list_length()
        len2 = list2.list_length()
        if len1 > len2:
            list2.pad_list(len1 - len2)
        else:
            list1.pad_list(len2 - len1)
        
            
        while list1head or list2head is not None:
            sum1 = carry + list1head.data + list2head.data
            if sum1 >= 10:
                summation.append(sum1%10)
                carry = int(sum1/10)
            else:
                summation.append(sum1)
            list1head = list1head.next
            list2head = list2head.next
        print("summation")
        for i in summation:
            print(i)
        print("///")
        listnew = SingleLinkedList()
        for i in summation:
            listnew.add_list_item(i)
        
        return listnew
    
    def pad_list(self,padding):
        for i in range(0,padding):
            self.add_list_item(0)
        return self
        
    def insert_before(self,data):
        node = ListNode(data)
        if self.head is not None:
            node.next = self.tail
        
        self.head = node
        #return self
    
    #2.6 Implement a function to check if a linked list is a palindrome
    
    def is_palinrome(self):
        currentNode = self.head
        list1 = []
        
        count = 0
        while currentNode is not None:
            list1.append(currentNode.data)
            currentNode = currentNode.next
        for i in list1:
            print(i)
        
        list2 = [0]*256
        for i in list1:
            list2[ord(str(i))] += 1
        for i in list2:
            if (i%2 != 0):
                count += 1
        if len(list1) % 2 == 0:
            if count == 0:
                return True
        else:
            if count == 1:
                return True
        
        return False
    #this implementation takes O(n) space
    def is_palindrome(self):
        if self.list_length() <= 1:
            return True
        currentNode = self.head
        list1 = []
        while currentNode is not None:
            list1.append(currentNode.data)
            currentNode = currentNode.next
        
        currentNode = self.head
        #print(list1[4])
        count = len(list1)
        i = count - 1
        for x in list1:
            print(x)
        while (i >= (count/2) ):
            if currentNode.data != list1[i]:
                return False
            currentNode = currentNode.next
            i -= 1
        
        return True
    
    def is_palindrome_recursive(self):
        #current = None
        """left = self.head     #its a instance variable declared at top
        result = self.helper(self.head)
        return result"""
        #if not self.head or self.head.next:
            #return True
        head = self.head
        SingleLinkedList.current = self.head
        #print(self.current.data)
        
        return SingleLinkedList.helper(head)
        
    
    @staticmethod#try the other method with splitting the list and reversing the other half and comparing 
    def helper(head):
        
        """if(right is None):
            return True
        x = self.helper(right.next)
        if(not x):
            return False
        y = (self.left.data == right.data)
        
        self.left = self.left.next"""
        
        if head is None:
            return True
        x = SingleLinkedList.helper(head.next)
        if not x:
            return False
        y = (SingleLinkedList.current.data == head.data)
        SingleLinkedList.current = SingleLinkedList.current.next            
        return y
    
    
        
    #2.8 loop detection: Given a loop in a linked list, return the node at beginning 
    #of the loop
    #i/p - a->b->c->d->e->c
    #o/p - c
    
    def detect_loop(self):
        slow = self.head
        fast = self.head
        result = False
        while fast is not None and fast.next is not None:
           slow = slow.next
           fast = fast.next.next
           if fast == slow:
               result = True
               break
        
            
        if result is False:
            return None
        else:
            slow = self.head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
                
    
    #2.7
    #Loop Intersection - Given two lists, check if two lists intersect and return the intersectingt node
    def detect_intersection(self,list2):
        l1head = self.head
        l2head = list2.head
        l1 = self.list_length()
        l2 = list2.list_length()
        
        if l1 >= l2:
            i = l1-l2
            while i > 0:
                l1head = l1head.next
                i -= 1
            while l1head is not None:
                if l1head == l2head:
                    return l1head
                l1head = l1head.next
                l2head = l2head.next
         
        else:
            i = l2-l1
            while i > 0:
                l2head = l2head.next
                i -= 1
            while l2head is not None:
                if l2head == l1head:
                    return l2head
                l1head = l1head.next
                l2head = l2head.next
            
        return None
                
        
        
                
       
            
        
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)
node7 = ListNode(7)
node8 = ListNode(8)

list1 = SingleLinkedList()

for item in [node1, node2, node3, node4, node5, node6, node7, node8]:
    list1.add_list_item(item)

list2 = SingleLinkedList()
for item in [node5, node6, node7, node8]:
    list2.add_list_item(item)


list1.tail.next = list1.head.next
list2.output_list()

print(list1.tail.next.data)
result = list1.detect_loop()
print(result.data)
#result = list1.is_palindrome()
#result = list1.is_palindrome_recursive()
result = list2.detect_intersection(list1)
print(result.data)
list1.list_length()
x = 10
z = 5
y = (x==z)
print(y)

#list1.delete_node(12)
#list1.remove_duplicates_without_buffer()

#x = list1.return_kth_to_last(2)
#print(x)
#list1.delete_middle_node(118)
#list1.output_list()

#listnew = list1.partition_list(5)
#listnew.output_list()

"""n1 = ListNode(7)
n2 = ListNode(1)
n3 = ListNode(6)
n4 = ListNode(5)
n5 = ListNode(9)
n6 = ListNode(2)

list2 = SingleLinkedList()
list3 = SingleLinkedList()


for item in [n2,n3]:
    list2.add_list_item(item)

for item in [n4,n5,n6]:
    list3.add_list_item(item)

list2.output_list()
list3.output_list()
print(list2.head.data)
listnew = list1.sum_lists(list2,list3)
listnew.output_list() 
print(list2.head.data)

list4 = SingleLinkedList()
for item in [n2,n3]:
    list4.add_list_item(item)
list4.output_list()
list4.insert_before(5)
list2.pad_list(1)
list1 = [1,2,3,4,5]
print(list1[4])"""
