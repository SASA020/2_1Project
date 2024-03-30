'''
The list is singly linked list, i.e. you can only have one link for each node.
The complexity of the reverse procedure should be O(n)
'''

class Node:
    def __init__(self, item):
        "=======STUDENT'S CODE======"
        self.item = item
        self.link = None
class LinkedList:
    def __init__(self):
        "=======STUDENT'S CODE======"
        self.head = None
        self.tail = None
    def add(self, item):
        "=======STUDENT'S CODE======"
        n = Node(item)
        if self.head == None: #빈리스트
            self.head = n
            self.tail = self.head

        elif self.head == self.tail: #원소가 하나일때
            self.head.link = n
            self.tail = n
        
        else:
            self.tail.link = n
            self.tail = n


    def print(self):
        "=======STUDENT'S CODE======"
        node = self.head
        while node:
            print(node.item, end= " ")
            node = node.link
        print()
        
    def reverse(self):
        "=======STUDENT'S CODE======"
        prev_node = None
        node = self.head

        while node:
            next_node = node.link
            node.link = prev_node
            prev_node = node
            node = next_node
        
        self.head = prev_node

