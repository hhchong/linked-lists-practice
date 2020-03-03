#implement an algorithm to find the kth to last element of a singly linked list
#two pointers, first one starts at kth place
#then move together w other at 0
#once orig pointer reaches end, then second pointer is at kth to last.

import unittest

def kth_to_last(head, k):

    
    pointer_1 = head

    pointer_2 = head

    for i in range(0, k):
        if pointer_1 is None:
            return None
        pointer_1 = pointer_1.next

    while pointer_1:
        pointer_1, pointer_2 = pointer_1.next, pointer_2.next
        #pointers keep goin till pointer_1 breaks while cause it's None
        #now pointer2 is at kth from end
    return pointer_2




class Node():
  def __init__(self, data, next=None):
    self.data = data
    self.next = next

class Test(unittest.TestCase):
  def test_kth_to_last(self):
    head = Node(1,Node(2,Node(3,Node(4,Node(5,Node(6,Node(7)))))))
    self.assertEqual(None, kth_to_last(head, 0));
    self.assertEqual(7, kth_to_last(head, 1).data);
    self.assertEqual(4, kth_to_last(head, 4).data);
    self.assertEqual(2, kth_to_last(head, 6).data);
    self.assertEqual(1, kth_to_last(head, 7).data);
    self.assertEqual(None, kth_to_last(head, 8));

unittest.main()