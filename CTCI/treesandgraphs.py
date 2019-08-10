#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 15:47:41 2019

@author: mayankraj

implementation of trees and graphs based on CTCI problems 
"""
import copy
class Node:
    def __init__(self,value):
        self.value = value
        self.left_child = None
        self.right_child = None
        

class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    def insert(self,item):
        if not isinstance(item,Node):
            item = Node(item)
            
        if self.root is None:
            self.root = item
        else:
            self._insert(item,self.root)
    
    def _insert(self,item, curr_node):
        if item.value < curr_node.value:
            if curr_node.left_child is None:
                curr_node.left_child = item
            else:
                self._insert(item, curr_node.left_child)
        elif item.value > curr_node.value:
            if curr_node.right_child is None:
                curr_node.right_child = item
            else:
                self._insert(item,curr_node.right_child )
        
        else:
            print("Value already exists in the tree")
    

    """
    4.2 
    Minimal tree
    Given a sorted array with unique integer elements,write an algorithm to create
    a search tree with minimal height
    Soln:
        Make the mid element the root , then recursively make the 
        left half mid elemnt left child and right half mid element 
        right child
    """

    def sorted_array_to_bst(self,arr):
        if not arr:
            return None
        
        mid = int(len(arr)/2)
        
        root = Node(arr[mid]) 
        
        root.left_child = self.sorted_array_to_bst(arr[:mid])
        #find left child as mid element of left part of array
        
        root.right_child = self.sorted_array_to_bst(arr[mid+1:])
        
        self.root = root
        return self.root
        
        
    def print_tree(self):
        #traversal = ""
        if self.root is not None:
            traversal = self._print_tree(self.root, "")
        
        return traversal
            
    def _print_tree(self,curr_node, traversal):
        if curr_node is not None:
            
            traversal = self._print_tree(curr_node.left_child, traversal)
            traversal += (str(curr_node.value) + "->")
            #print(str(curr_node.value))
            traversal = self._print_tree(curr_node.right_child, traversal)
        return traversal
    
    def search(self,curr_node,key):
        if curr_node is None or curr_node.value == key:
            return curr_node
        if curr_node.value > key:
            return self.search(curr_node.left_child , key)
        return self.search(curr_node.right_child , key)
    
    """
    4.6 Write an algorithm to find the next node(successor node) of a given
    node in a binary search tree. You may assume that each node has a link
    to its parent
    """
    
    def next_node(self,nodeValue):
        
        curr_node = self.search(self.root,nodeValue)
        #print(curr_node.value)
        if curr_node is not None:
            if curr_node.right_child is not None:
                return self._leftMost_node(curr_node.right_child)
        
        head = self.root
        successor = Node(None)
        while head  is not None:
            if head.value > nodeValue:
                successor = head 
                head  = head.left_child
            elif head.value < nodeValue:
                head  = head.right_child
            else:
                return successor
        return None
                
    
    def _leftMost_node(self,node):
        while node.left_child is not None:
            node = node.left_child
        return node
    
        

class BinaryTree:
    def __init__(self,root):
        self.root = Node(root)
    
    def insert(self,item):
        if not isinstance(item,Node):
            item = Node(item)
        
        if self.root is None:
            self.root = item
        else:
            self._insert(item,self.root)
    
    def _insert(self,item,curr_node):
        
        que = []
        que.append(curr_node)
        
        while que is not None:
            curr_node = que[0]
            que.pop(0)
            
            if not curr_node.left_child:
                curr_node.left_child = item
                break
            else:
                que.append(curr_node.left_child)
            
            if not curr_node.right_child:
                curr_node.right_child = item
                break
            else:
                que.append(curr_node.right_child)
                
    
    def print_tree(self,traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(self.root,"")
        if traversal_type == "inorder":
            return self.inorder_print(self.root,"")
        if traversal_type == "postorder":
            return self.postorder_print(self.root,"")
        else:
            print("Traversal type" + str(traversal_type) + "is not supported")
            return False
        
    
    def preorder_print(self, start, traversal):
        """
        using traversal as a string to print out values
        Root -> Left -> Right
        """
        if start:
            traversal += (str(start.value) + "->")
            traversal = self.preorder_print(start.left_child, traversal)
            traversal = self.preorder_print(start.right_child, traversal)
            
        return traversal
    
    def inorder_print(self, start, traversal):
        """
        left -> root -> right
        """
        if start:
            traversal = self.inorder_print(start.left_child,traversal)
            traversal += (str(start.value) + "->")
            traversal = self.inorder_print(start.right_child, traversal)
        
        return traversal
     
    def postorder_print(self, start, traversal):
        """
        left -> right -> root
        """
        if start:
            traversal = self.postorder_print(start.left_child, traversal)
            traversal = self.postorder_print(start.right_child, traversal)
            traversal += (str(start.value) + "->")
            
        return traversal


    """
    4.4 Check Balanced:
    Implement a function to check if a binary tree is balanced or not. A balanced
    tree is one such that heights of two subtrees of any node does not differ 
    by more than one
    
    1. First check if left subtree is height balanced, if yes, then return its
    height to node n or return -1
    2. Do same with right subtree for node n
    3.Finally we check if the tree is heoght balanced for node n by checking
    the difference between h_left and h_right. If it is balanced we return
    max of the heights + 1. 
    4.If node n is null,then we return 0(base case for the recursion)

    """
    
    def isBalanced(self):
        if (self._treeheight(self.root) > -1):
            return True
        return False
        
        
    def _treeheight(self,curr_node):
        if curr_node is None:
            return 0
        height_left_subtree = self._treeheight(curr_node.left_child)
        height_right_subtree = self._treeheight(curr_node.right_child)
        
        if height_left_subtree == -1 or height_right_subtree == -1:
            return -1
        if abs( height_left_subtree - height_right_subtree) > 1:
            return -1
        if height_left_subtree > height_right_subtree:  
            return height_left_subtree + 1
        return height_right_subtree + 1


def fill_tree(tree, num_elem = 100, max_int = 1000):
    from random import randint
    for _ in range(num_elem):
        cur_elem = randint(0, max_int)
        tree.insert(cur_elem)
    return tree
"""
Implemntation of a graph using adjecency list

""" 
class Vertex:
    def __init__(self,item):
        self.item = item
        self.neighbors = list()
    
    def add_neighbor(self,item):
        if item not in self.neighbors:
            self.neighbors.append(item)
            self.neighbors.sort()

class Graph():
    vertices = {}
    
    def add_vertex(self,vertex):
        if not isinstance(vertex,Vertex):
            vertex = Vertex(vertex)
        if isinstance(vertex, Vertex) and vertex.item not in self.vertices:
            self.vertices[vertex.item] = vertex #dict[key] = value
            return True
        else:
            return False
        
    def add_edge(self,u,v):
        if u in self.vertices and v in self.vertices:
            for key,value in self.vertices.items():
                if key == u:
                    value.add_neighbor(v)
                if key == v:
                    value.add_neighbor(u)
            return True
        else:
            return False
    
    def add_edge_directed(self,u,v):
        if u in self.vertices and v in self.vertices:
            for key,value in self.vertices.items():
                if key == u:
                    value.add_neighbor(v)
            return True
        else:
            return False
        
    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key+str(self.vertices[key].neighbors))
            
    def is_reachable(self,u,v,search_type):
        #here using list as stack
        if search_type == "DFS":
            visited = set()
            result = self._dfs(u,v,visited)
        else:
            
            result = self._bfs(u,v)
        
        return result
    
    def _bfs(self,u,v):
        queue = []
        queue.append(u)
        visited = set()    #set
        visited.add(u)
        #print(type(u))
        #print(u.neighbors)
        #print(stack.pop())
        #stack.append(u)
        while queue:
            
            x = queue.pop(0)
            if x == v:
                return True
            
            
            neighbors = self.vertices[x].neighbors
            for neighbor in neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
                """else:
                    if neighbor not in visited:
                        stack.append(neighbor)
                        visited.add(neighbor)
                    """
    
        return False
    
    def _dfs(self,u,v,visited):
        if u == v:
            return True
        #visited = set()
        visited.add(u)
        for neighbor in self.vertices[u].neighbors:
            if neighbor not in visited:
                if self._dfs(neighbor,v,visited):
                    return True
        return False

    def list_toGraph(self,list1):
        for item in list1:
            for items in item:
                self.add_vertex(items)
        
        for item in list1:
            self.add_edge_directed(item[0],item[1])
            
        self.print_graph()
        
        
    """
    4.7 Build order
    
    You are given a list of projects and a list of dependencies(which is a 
    list of projects in which 2nd oneis depended on the 1st one. All of project 
    dependencies must be build before the project is). find an order which allows 
    the projects to build, and if there 
    is no valid build order then return error
    
    Sol - this is similar to topological sorting in DAG(Directed Acyclic Graph). 
    If the graph is not DAG then topological sorting cannot be done 
    """
    def topological_sort(self):
        visited = set()
        temp_stack = []
        
        for key,value in self.vertices.items():     #key is vertex value, value is actual node of graph
            if key not in visited:
                self._util_topo(key,temp_stack,visited)

        return temp_stack
    
    def _util_topo(self,vertex,stack,visited):
        visited.add(vertex)
        for neighbor in self.vertices[vertex].neighbors:
            if neighbor not in visited:
                self._util_topo(neighbor,stack,visited)
        stack.append(vertex)  
        
        
        


"""
implementation of a undirected graph using adjacency matrix qith weighted 
or unweighted edges


"""
"""class Vertex:
    def __init__(self,item):
        self.item = item
        
class Graph:
   
        
    vertices = {}
    edges = []
    edge_indices = {}
    
    
    def add_vertex(self,vertex):
        if isinstance(vertex,Vertex) and vertex.item not in self.vertices:
            self.vertices[vertex.item] = vertex
            for row in self.edges:
                row.append(0)
            self.edges.append([0]*(len(self.edges) +1))
            self.edge_indices[vertex.item] = len(self.edge_indices)
            return True
        else:
            return False
        
    def add_edges(self,u,v, weight = 1):
        if u in self.vertices and v in self.vertices:
            self.edges[self.edge_indices[u]][self.edge_indices[v]] = weight
            self.edges[self.edge_indices[v]][self.edge_indices[u]] = weight
            return True
        else:
            return False
        
    def print_graph(self):
        for v, i in sorted(self.edge_indices.items()):
            print(v +"", end = "")
            for j in range(len(self.edges)):
                print(self.edges[i][j],end = "")
                print(" ")
 """       



"""
4.3 List of Depths:
    Given a binary tree, design an algorithm which creates a linked list of all
    the nodes at each depth (If you have a tree of depth D, then there should
    be D lists)
    
    
    All power of two numbers have only one bit set. So count the no. of set 
    bits and if you get 1 then number is a power of 2. Please see Count set
    bits in an integer for counting set bits.

    If we subtract a power of 2 numbers by 1 then all unset bits after 
    the only set bit become set; and the set bit become unset.

"""

def list_of_depths(tree):
    queue = []
    queue.append(tree.root)
    tempList = [[] for i in range(10)]
    i = 0
    while queue:
        if len(queue) != 0 and ((len(queue) & (len(queue) - 1)) == 0):
            tempList[i] = copy.deepcopy(queue)
            i += 1
        curr_node = queue[0]
        queue.pop(0)
        
        if curr_node.left_child:
            queue.append(curr_node.left_child)
        if curr_node.right_child:
            queue.append(curr_node.right_child)
    
    maxm = -999
    index = 0
    for j in tempList:
        if len(j) >= maxm:
            maxm = len(j)
            index += 1
    for i in range(index,len(tempList) -1):
        while len(tempList[i]) > 0:
            tempList[i].pop()
    
    return tempList
        
"""

4.5 Validate BST

Check if a given Binary Tree is also a Binary Search Tree


"""
def is_binary_tree_also_search_tree(treeInstance):
    minm = -9999
    maxm = 9999
    return check_BST(treeInstance.root,minm,maxm)

def check_BST(curr_node,minm,maxm):
    
    if curr_node is None:
        return True
    if curr_node.value <= minm and curr_node.value >= maxm:
        return False
    
    return check_BST(curr_node.left_child, minm, curr_node.value) and check_BST(curr_node.right_child,curr_node.value, maxm)



    




a = Vertex("A")
b = Vertex("B")
c = Vertex("C")
d = Vertex("D")
e = Vertex("E")
f = Vertex("F")
g = Graph()
list1 = [["a","d"],["f","b"],["b","d"],["f","a"],["d","c"]]
g.list_toGraph(list1)
x = g.topological_sort()
for i in [a,b,c,d,e,f]:
    g.add_vertex(i)

g.add_edge_directed(a.item,b.item)
g.add_edge_directed(a.item,c.item)
g.add_edge_directed(b.item,d.item)
g.add_edge_directed(b.item,e.item)
g.add_edge_directed(e.item,c.item)
g.add_edge_directed(f.item,d.item)
g.add_edge_directed(f.item,e.item)

g.print_graph()

x = g.is_reachable(a.item,e.item,"DFS") 

tree = BinarySearchTree()
tree = fill_tree(tree)
print(tree.print_tree())



"""
    preorder = 1->2->4->5->3->6->7 
    inorder = 4->2->5->1->6->3->7
    postorder = 4->5->2->6->7->3->1
            1
        /     \
        2      3
        /\     /\
       4  5    6 7


"""
bst = BinarySearchTree()
arr = [1,2,3,4,5,6,7,8,9,10]
bst.sorted_array_to_bst(arr)
bst.print_tree()
x = bst.next_node(1)
print(x.value)

result = is_binary_tree_also_search_tree(bst)

x = list_of_depths(tree) 
for i in x:
    for j in i:
        print(j)
tree = BinaryTree(1)
for i in [2,3,4,5,6,7,8,9,10,11,12,13]:
    tree.insert(i)


tree.root.left_child = Node(2)
tree.root.left_child.left_child = Node(3)
tree.root.left_child.left_child = Node(4)
tree.root.left_child.right_child = Node(5)
tree.root.right_child.left_child = Node(6)
tree.root.right_child.right_child = Node(7)

print(tree.print_tree("preorder"))
print(tree.print_tree("inorder"))
print(tree.print_tree("postorder"))

