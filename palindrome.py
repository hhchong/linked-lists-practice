#implement a function to check if a linked list is a palindrome.

#slow pointer and fast pointer
#go to the middle of a list - fast traverses twice as fast, so by the end of linked list slow pointer will be in the middle
#reverse the second half
#compare the first and second half nodes



import unittest

def is_palindrome(head):

    #start at head
    fast = slow = head

    #get the mid node, fast traverses twice as fast
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    #reverse the second half
    #nodes are in place, the pointers reverse
    prev = None
    while slow:
        #nxt is the next node after slow
        nxt = slow.next
        #slow.next pointer reverses to prev
        slow.next = prev
        #prev node moves to the place or orig slow
        prev = slow
        #slow node moves to the place of nxt
        slow = nxt

    #check if reversed part is same as first part
    while prev:
        if prev.data != head.data:
            return False
        prev = prev.next
        head = head.next
    return True


#O(n) time O(1) extra space

class Node():
  def __init__(self, data, next=None):
    self.data, self.next = data, next

  def __str__(self):
    string = str(self.data)
    if self.next:
      string += ',' + str(self.next)
    return string

class Test(unittest.TestCase):
  def test_palindrome(self):
    list1 = Node(10)
    self.assertTrue(is_palindrome(list1))
    list2 = Node(10,Node(10))
    self.assertTrue(is_palindrome(list2))
    list3 = Node(10,Node(20))
    self.assertFalse(is_palindrome(list3))
    list4 = Node(10,Node(70,Node(30,Node(70,Node(10)))))
    self.assertTrue(is_palindrome(list4))
    
 

unittest.main()