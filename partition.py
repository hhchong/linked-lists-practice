#write code to partition a linked list around a value x, such that all nodes less than x come before all nodes greater than or equal to x. 

#use head and tail.. traverse list, if node is < head, push it, if node is >, append to tail?

import unittest

def partition(head, p):
    node = head
    head_new = None
    head_greater = None
    tail_greater = None
    tail_new = None

    while node:
        
        if node.data < p:
            if head_new == None:
                head_new = node
                tail_new = node
            else:
                tail_new.next = node
                tail_new = node
             
        else:
            if head_greater is None:
                head_greater = node
                tail_greater = node
            else:
                tail_greater.next = node
                tail_greater = node
        node = node.next
    tail_new.next = head_greater
    return head_new


class Node():
  def __init__(self, data, next=None):
    self.data, self.next = data, next
  
  def __str__(self):
    string = str(self.data)
    if self.next:
      string += ',' + str(self.next)
    return string

class Test(unittest.TestCase):
  def test_partition(self):
    head1 = Node(7,Node(2,Node(9,Node(1,Node(6,Node(3,Node(8)))))))
    head2 = partition(head1, 6)
    self.assertEqual(str(head2), "2,1,3,7,9,6,8")
    head3 = partition(head2, 7)
    self.assertEqual(str(head3), "2,1,3,6,7,9,8")

unittest.main()