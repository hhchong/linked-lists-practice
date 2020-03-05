#given a linked list which might contain a loop, implement an algorithm that returns the node at the beginning of the loop (if one exists)

#a -> b -> c -> d -> e -> c
#c
import unittest

def detect_cycle(head):

    #use a seen hash map
    #two pointers, one before one after

    pA = head
    pB = head.next

    seen = {}

    while pB is not None:
        seen[pA] = 1
        #add pA to hm, use it to quickly check if pB is there
        if pB in seen:
            return pB
        #else, keep traversing
        pA = pA.next
        pB = pB.next

    return None






class Node():
  def __init__(self, data, next=None):
    self.data, self.next = data, next

class Test(unittest.TestCase):
  def test_detect_cycle(self):
    head1 = Node(100,Node(200,Node(300)))
    self.assertEqual(detect_cycle(head1), None)
    node1 = Node(600)
    node2 = Node(700,Node(800,Node(900,node1)))
    node1.next = node2
    head2 = Node(500,node1)
    self.assertEqual(detect_cycle(head2), node1)

unittest.main()