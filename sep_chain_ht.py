
class MyHashTable:

    def __init__(self, table_size=11):
        self.table_size = table_size
        self.hash_table = [[] for _ in range(table_size)] # List of lists implementation
        self.num_items = 0
        self.num_collisions = 0

    def insert(self, key, value):
        "Takes a key, and an item.  Keys are valid Python non-negative integers. \
        The function will insert the key-item pair into the hash table based on the \
        hash value of the key mod the table size (hash_value = key % table_size)"

    def get_item(self, key):
        "Takes a key and returns the item from the hash table associated with the key. \
        If no key-item pair is associated with the key, the function raises a LookupError exception."

    def remove(self, key):
        "Takes a key, removes the key-item pair from the hash table and returns the key-item pair. \
        If no key-item pair is associated with the key, the function raises a LookupError exception. \
        (The key-item pair should be returned as a tuple)"

    def load_factor(self):
        "Returns the current load factor of the hash table"

    def size(self):
        "Returns the number of key-item pairs currently stored in the hash table"

    def collisions(self):
        "Returns the number of collisions that have occurred during insertions into the hash table"

