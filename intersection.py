#given two singly linked lists, determine if the two lists intersect. Return the intersecting node. 
import unittest

def intersection(head1, head2):

#traverse both linked lists; once at the end, traverse other list 
    if head1 is None or head2 is None:
        return None

    pointer_1 = head1
    pointer_2 = head2

    while pointer_1 != pointer_2:

        pointer_1 = head2 if pointer_1 is None else pointer_1.next
        pointer_2 = head1 if pointer_2 is None else pointer_2.next

    return pointer_1

    
class Node():
  def __init__(self, data, next=None):
    self.data, self.next = data, next

  def __str__(self):
    string = str(self.data)
    if self.next:
      string += ',' + str(self.next)
    return string

class Test(unittest.TestCase):
  def test_intersection(self):
    head1 = Node(10,Node(20,Node(30)))
    head2 = Node(20,Node(30,Node(40)))
    self.assertEqual(intersection(head1, head2), None)
    node = Node(70,Node(80))
    head3 = Node(50,Node(20,node))
    head4 = Node(60,Node(90,Node(10,node)))
    self.assertEqual(intersection(head3, head4), node)

unittest.main()