#Write code to remove duplicates from an unsorted linked list. 

#traverse the linked list as many times as the # of n to see if there are matches, then delete
#or add a dictionary as a seen, if node in seen, delete.

import unittest

def remove_duplicates(head):

    nodes = {}

    node = head

    while node is not None:
        if node.data in nodes.keys():
            node.data = node.next.data
            node.next = node.next.next
        else:
            nodes[node.data] = 1
            node = node.next

    return head


class Node():
  def __init__(self, data, next):
    self.data = data
    self.next = next

class Test(unittest.TestCase):
  def test_remove_duplicates(self):
    head = Node(1,Node(3,Node(3,Node(1,Node(5,None)))))
    remove_duplicates(head)
    self.assertEqual(head.data, 1)
    self.assertEqual(head.next.data, 3)
    self.assertEqual(head.next.next.data, 5)
    self.assertEqual(head.next.next.next, None)


unittest.main()