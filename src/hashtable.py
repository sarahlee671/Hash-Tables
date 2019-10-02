# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity
        self.count = 0


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        hash = 5381
        for x in self.storage:
            hash = (( hash << 5) + hash) + ord(x)

        return x % self.capacity
       

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        print a warning 

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        index = self._hash_mod(key)
        if self.storage[index] is not None:
            pair = self.storage[index]
            #if the bucket is filled, chain 
            while pair is not None:
                if pair.key is key:
                    pair.value = value
                    break
                elif pair.next is None:
                    pair.next = LinkedPair(key, value)
                    break
                else:
                    pair= pair.next

        else:
            self.storage[index] = LinkedPair(key, value)





    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''

        index = self._hash_mod(key)

        if self.storage[index] is None:
            print("Warning: Key not found")
            return
        
        curr = self.storage[index]
       
        while curr is not None:
            if curr.key == key:
                self.storage[index] = None
                break
            else:
                curr = curr.next



    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        pair = self.storage[index]

        if pair is not None:
            curr = self.storage[index]

            while curr is not None:
                if curr.key is key:
                    return curr.value
                else:
                    curr = curr.next

            else:
                return None
        


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        self.capacity *= 2
        new_storage = [None] * self.capacity
        copy_storage = self.storage
        self.storage = new_storage

        for pair in copy_storage:
            if pair is not None:
                curr = pair
                while curr is not None:
                    self.insert(curr.key, curr.value)
                    curr = curr.next
        




if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    #test remove
    # ht.remove("line_3")
    # ht.remove("line_3")

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
