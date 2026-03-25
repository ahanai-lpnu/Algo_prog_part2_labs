import unittest
from lab4 import RedBlackPriorityQueue

class TestRedBlackPriorityQueue(unittest.TestCase):

    def setUp(self):
        self.pq = RedBlackPriorityQueue()

    def test_insert_and_peek(self):
        self.pq.insert("Low", 10)
        self.pq.insert("High", 100)
        self.pq.insert("Medium", 50)
        
        val, prio = self.pq.peek()
        self.assertEqual(val, "High")
        self.assertEqual(prio, 100)

    def test_pop_order(self):
        elements = [("Task A", 15), ("Task B", 3), ("Task C", 99), ("Task D", 42)]
        for val, prio in elements:
            self.pq.insert(val, prio)
 
        expected_order = [99, 42, 15, 3]
        actual_order = []
        
        while self.pq.peek() is not None:
            _, prio = self.pq.pop()
            actual_order.append(prio)
            
        self.assertEqual(actual_order, expected_order)

    def test_duplicate_priorities(self):
        self.pq.insert("Task 1", 50)
        self.pq.insert("Task 2", 50)
        
        val1, prio1 = self.pq.pop()
        val2, prio2 = self.pq.pop()
        
        self.assertEqual(prio1, 50)
        self.assertEqual(prio2, 50)
        self.assertTrue(val1 in ["Task 1", "Task 2"]) 

    def test_empty_queue_pop(self):
        with self.assertRaises(IndexError):
            self.pq.pop()

    def test_peek_empty(self):
        self.assertIsNone(self.pq.peek())

if __name__ == '__main__':
    unittest.main()