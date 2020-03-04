#you have two numbers represented by a linked list, where each node contains a single digit. The digits are stored in reverse order, such that the 1's digit is at the head of the list. Write a function that adds the two numbers and returns the sum as a linked list. 
import unittest


def sum_lists(num1, num2):

    carry = 0
    p = num1
    q = num2
    result = Node(0)
    result_tail = result

    while p or q or carry:
        x = (int(p.data) if p else 0)
        y = (int(q.data) if q else 0) 
        total = x + y + carry
        carry = int(total/10)

        result_tail.next = Node(total % 10)
        result_tail = result_tail.next
        p = (p.next if p else None)
        q = (q.next if q else None)
    # if carry == 1:
    #     result_tail.next = 1
    #     result_tail = result_tail.next


    return result.next

class Node(object):
  def __init__(self, data, next=None):
    self.data, self.next = data, next
  
  def __str__(self):
    string = str(self.data)
    if self.next:
      string += ',' + str(self.next)
    return string



    
class Test(unittest.TestCase):
  def test_sum_lists(self):
    num1 = Node(1,Node(2,Node(3)))
    num2 = Node(4,Node(9,Node(5)))
    self.assertEqual(str(sum_lists(num1, num2)), "5,1,9")
    num1 = Node(9,Node(2,Node(3,Node(4,Node(1)))))
    num2 = Node(4,Node(9,Node(8)))
    self.assertEqual(str(sum_lists(num1, num2)), "3,2,2,5,1")

unittest.main()


