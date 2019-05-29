import unittest
from sep_chain_ht import *

class TestList(unittest.TestCase):

   def test_insert1(self):
      hash1 = MyHashTable()
      hash1.insert(11, "a") 
      hash1.insert(3, "b")
      self.assertEqual(hash1.size(), 2)

   def test_insert2(self):
      hash1 = MyHashTable(2)
      hash1.insert(11, 'a')
      hash1.insert(12, 'b')
      hash1.insert(13, 'c')
      hash1.insert(14, 'd')
      self.assertEqual(hash1.table_size, 5)
      

   def test_get1(self):
      hash1 = MyHashTable(5)
      hash1.insert(11, "a")
      hash1.insert(3, "b")
      self.assertEqual(hash1.get_item(3), 'b')
      self.assertEqual(hash1.get_item(11), 'a')
      
   def test_get2(self):
      hash1 = MyHashTable(5)
      hash1.insert(11, "a")
      with self.assertRaises(LookupError):
            hash1.get_item(6)

   def test_remove1(self):
      hash1 = MyHashTable(5)
      hash1.insert(11, "a")
      hash1.insert(12, 'v')
      hash1.insert(2, 's')
      self.assertEqual(hash1.remove(11), (11, 'a'))
      self.assertEqual(hash1.size(), 2)
      with self.assertRaises(LookupError):
            hash1.remove(6)

   def test_load_factor1(self):
      hash1 = MyHashTable(5)
      hash1.insert(11, "a")
      hash1.insert(3, "b")
      hash1.insert(1, "c")
      hash1.insert(8, "d")
      hash1.insert(4, "e")
      hash1.insert(5, "f")
      hash1.insert(1, "g")
      hash1.insert(2, "h")
      self.assertEqual(hash1.load_factor(), 1.4)

   def test_collisions2(self):
      hash1 = MyHashTable(5)
      hash1.insert(11, "a") 
      hash1.insert(3, "b") 
      hash1.insert(1, "c") 
      hash1.insert(8, "d") 
      hash1.insert(4, "e") 
      hash1.insert(5, "f") 
      hash1.insert(1, "g") 
      hash1.insert(2, "h")
      self.assertEqual(hash1.collisions(), 2)

if __name__ == '__main__': 
   unittest.main()


